from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional, Annotated
from fastapi import FastAPI, Depends
from app.settings import DATABASE_URL

# Define the UserBase and User models
class UserBase(SQLModel):
    user_name: str
    user_address: str
    user_email: str
    user_password: str

class User(UserBase, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)

# Set up the database connection
connection_string = str(DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)
engine = create_engine(
    connection_string, connect_args={}, pool_recycle=300
)

# Function to create the database and tables
async def create_db_and_tables(app: FastAPI):
    print(f'Create Tables ...  {app} ')
    SQLModel.metadata.create_all(engine)
    yield

# Dependency to get a session
def get_session():
    with Session(engine) as session:
        yield session

DB_Session = Annotated[Session, Depends(get_session)]

# Create FastAPI instance
app = FastAPI(lifespan= create_db_and_tables)

@app.get('/')
def root_route():
    return {"Welcome to": "User Service"}

# Function to add a user into the database
def add_user_into_db(form_data: UserBase, session: Session):
    user = User(**form_data.dict())  # Use dict() to convert Pydantic model to dict
    session.add(user)
    session.commit()
    session.refresh(user)
    print("New user added:", user)
    return user

# POST route to add a new user
@app.post('/api/add_user')
def add_user(new_user: UserBase, session: DB_Session):
    added_user = add_user_into_db(new_user, session)
    print("add user route ...", add_user)
    return added_user


















  





