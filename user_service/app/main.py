from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional, Annotated
from fastapi import FastAPI, Depends, HTTPException
from pydantic import EmailStr
from app.settings import DATABASE_URL

### ========================= *****  ========================= ###

#Create Database Schema using SQLMode

# Define the UserBase and User models
class UserBase(SQLModel):
    user_name: str
    user_address: str
    user_email: EmailStr
    user_password: str    

class User(UserBase, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)

class UserUpdateModel(SQLModel):
    user_name: str
    user_address: str
    user_password: str  

### ========================= *****  ========================= ###

# Set up the database connection
connection_string = str(DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)

# Create an engine for the database connection
engine = create_engine(
    connection_string, connect_args={}, pool_recycle=300
)

# Function to create the database and tables
async def create_db_and_tables():
    print(f'Creating Tables ...')
    # Create all the database tables
    SQLModel.metadata.create_all(engine)

# function, before the yield, will be executed before the application starts
# create session to get memory space in db
def get_session():
    with Session(engine) as session:
        yield session

# Dependency injection to get a session
DB_Session = Annotated[Session, Depends(get_session)]

### ========================= *****  ========================= ###

# Lifespan function provided by FastAPI (creates DB table at program startup)
# It creates the table only once; if the table already exists, it won't create it again
async def life_span(app: FastAPI):
    print("Call create tables function during lifespan startup...")
    await create_db_and_tables()  # Properly await table creation
    yield  # Lifespan generator is working correctly

# Create FastAPI instance
app = FastAPI(lifespan=life_span, title='Product API')


@app.get('/')
def root_route():
    return {"Welcome to": "User Service"}

### ========================= *****  ========================= ###

# Function to retrieve user data from the database
def get_user_from_db(session: DB_Session):
    # Create a SQL statement to select all users
    statement = select(User)
    # Execute the statement and get the list of users
    user_list = session.exec(statement).all()

    # If no users found, raise an HTTPException with status code 404
    if not user_list:
        raise HTTPException(status_code=404, detail="Not Found")
    # Otherwise, return the list of users
    else:
        return user_list


# API endpoint to get users
@app.get('/api/get_user')
def get_user(session: DB_Session):
    # Call the function to retrieve user data from the database
    users = get_user_from_db(session)
    # Return the list of users
    return users

### ========================= *****  ========================= ###

# Function to add a user into the database
def add_user_into_db(form_data: UserBase, session: Session):
    # Create a new User object using the details provided in form_data
    user = User(**form_data.model_dump())

    # Add the user to the session
    session.add(user)
    # Commit the session to save the user to the database
    session.commit()
    # Refresh the session to retrieve the new user data
    session.refresh(user)
    print("New user added:", user)
    return user


# POST route to add a new user
@app.post('/api/add_user')
def add_user(new_user: UserBase, session: DB_Session):
    # Call function to add user
    add_user = add_user_into_db(new_user, session)
    print("Add user route ...", add_user)
    return add_user

### ========================= *****  ========================= ###

def update_user_from_db(selected_id: int, update_form_data: UserUpdateModel, session: DB_Session):
    # Create a SQL statement to select the user with the given ID
    statement = select(User).where(User.user_id == selected_id)
    # Execute the statement and get the selected user
    selected_user = session.exec(statement).first()

    # If the user is not found, raise an HTTPException with status code 404
    if not selected_user:
        raise HTTPException(status_code=404, detail="Not Found")
    
    # Update the user's details with the data from the form
    # databse               = form data
    selected_user.user_name = update_form_data.user_name
    selected_user.user_password = update_form_data.user_password
    selected_user.user_address = update_form_data.user_address

    # Add the updated user to the session
    session.add(selected_user)
    # Commit the session to save the changes to the database
    session.commit()
    # Refresh the session to retrieve the updated user data
    session.refresh(selected_user)
    return selected_user


@app.put('/api/update_user')
def update_user(id:int, user_detail: UserUpdateModel, session: DB_Session):
    # Call the function to retrieve data from the database
    user = update_user_from_db(id, user_detail, session)
    return user

### ========================= *****  ========================= ###

# Function to delete a user from the database
def delete_user_from_db(delete_id: int, session: DB_Session):
    # Retrieve the user from the database using the given ID
    user = session.get(User, delete_id)

    # If the user is not found, raise an HTTPException with status code 404
    if not user:
        raise HTTPException(status_code=404, detail="Not Found")
    
    # Delete the user from the session
    session.delete(user)
    # Commit the session to save the changes to the database
    session.commit()
    return 'User deleted'

# API endpoint to delete a user
@app.delete('/api/delete_user')
def delete_user(id: int, session: DB_Session):
    # Call function to delete the user from the database
    deleted_user = delete_user_from_db(id, session)
    return f'User id {id} has been successfully deleted'

### ========================= *****  ========================= ###

