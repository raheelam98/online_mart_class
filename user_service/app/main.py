from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional, Annotated
from fastapi import FastAPI, Depends, HTTPException
from app.settings import DATABASE_URL

# Define the UserBase and User models
class UserBase(SQLModel):
    user_name: str
    user_address: str
    user_email: str
    user_password: str    

class User(UserBase, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)

class UserUpdateModel(SQLModel):
    user_name: str
    user_address: str
    user_password: str  


# Set up the database connection
connection_string = str(DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)

# Create an engine for the database connection
engine = create_engine(
    connection_string, connect_args={}, pool_recycle=300
)

# Function to create the database and tables
async def create_db_and_tables(app: FastAPI):
    print(f'Create Tables ...  {app} ')
    # create all the database tables
    SQLModel.metadata.create_all(engine)
    yield

# create session to get memory space in db
def get_session():
    with Session(engine) as session:
        yield session

# Dependency injection to get a session
DB_Session = Annotated[Session, Depends(get_session)]

# lifespan function provide by FastAPI (create db table at start of program)
# function, before the yield, will be executed before the application starts.
# it create table only one-time, if table is already created, won't create again
# Create FastAPI instance
app = FastAPI(lifespan= create_db_and_tables)

@app.get('/')
def root_route():
    return {"Welcome to": "User Service"}

# Function to add a user into the database
def add_user_into_db(form_data: UserBase, session: Session):
<<<<<<< HEAD
    user = User(**form_data.dict())  # Use dict() to convert Pydantic model to dict
=======
    user = User(**form_data.model_dump())  # Use dict() to convert Pydantic model to dict
>>>>>>> be1e33e (product_service)
    
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
    add_user = add_user_into_db(new_user, session) ## call function
    print("add user route ...", add_user)
    return add_user

# Function to retrive data from db
def get_user_from_db(session: DB_Session):
    statement = select(User)
    user_list = session.exec(statement).all()
    if not user_list:
        raise HTTPException(status_code=404, detail="Not Found")
    else:
        return user_list
    
# api :- get user
@app.get('/api/get_user')   
def get_user(session: DB_Session):
    users = get_user_from_db(session)
    return users

def update_user_from_db(selected_id: int , update_form_data: UserUpdateModel, session: DB_Session ):
    
    statement = select(User).where(User.user_id == selected_id)
    selected_user = session.exec(statement).first()
    if not selected_user:
        raise HTTPException(status_code=404, detail="Not Found")
    
    # from database         =   form data
    selected_user.user_name = update_form_data.user_name
    selected_user.user_password = update_form_data.user_password
    selected_user.user_address = update_form_data.user_address

    session.add(selected_user)
    session.commit()
    session.refresh(selected_user)
    return selected_user

@app.put('/api/update_user')
def update_user(id:int, user_detail: UserUpdateModel, session: DB_Session):
    user = update_user_from_db(id, user_detail, session)
    return user

# function to delete
def delete_user_from_db(delete_id:int, session: DB_Session):
    user = session.get(User, delete_id)
    if not user:
        raise HTTPException(status_code=404, detail="Not Found")
    
    session.delete(user)
    session.commit()
    return f'User deleted'

# api
@app.delete('/api/delete_user')
def delete_user(id:int, session: DB_Session):
    deleted_user = delete_user_from_db(id, session)
    return f'User {deleted_user} has been successfully deleted'
<<<<<<< HEAD








=======
>>>>>>> be1e33e (product_service)


### ========================= *****  ========================= ###
### ========================= *****  ========================= ###

# def delete_todo(id: int, session: Session):
#     # Retrieve the todo object with the given ID
#     todo = session.get(Todos1, id)
#     # If no todo found, return a message
#     if not todo:
#         return f"Could not find todo from ID: {id}"
#     # Delete the todo from the session
#     session.delete(todo)
#     # Commit the transaction to the database
#     session.commit()
#     # Retrieve all todos from the database
#     allTodos = session.exec(select(Todos1)).all()

# @app.delete("/deleteTodo")
# async def deleteTodo(todo_id: int, session: Annotated[Session, Depends(get_session)]):
#     todos = delete_todo(todo_id, session)
#     if not type(todos) == str:
#         return todos
#     raise HTTPException(status_code=404, detail=todos)

### ========================= *****  ========================= ###
### ========================= *****  ========================= ###




### ========================= *****  ========================= ###
### ========================= *****  ========================= ###
### ========================= *****  ========================= ###

# # lifespan function provide by FastAPI (create db table at start of program)
# # function, before the yield, will be executed before the application starts.
# # it create table only one-time, if table is already created, won't create again
# @asynccontextmanager
# async def life_span(app: FastAPI):
#     print("Creating Tables....")
#     create_db_table()
#     yield

# app = FastAPI(lifespan= life_span, title="API DB")

### ========================= *****  ========================= ###

# create session to get memory space in db

# create object of session and pass engine in it and return in local-variable session
# get-session is created on server.  (engine give db connectivity) 
# def get_session():
#     with Session(engine) as session:
#         yield session

### ========================= *****  ========================= ###

# # create engine
# engine = create_engine(connection_string, connect_args={"sslmode":"require"}, pool_recycle=300, echo=True)
# #  engine with echo=True, it will show the SQL it executes in the output

### ========================= *****  ========================= ###


### ========================= *****  ========================= ###
















  





