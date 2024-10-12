# online mart - user service

poetry —-version

**Create Poetry Project**

```bash
poetry new project_name 
```

add drivers mac
```shell
poetry add fastapi uvicorn\[standard\] 
```

add drivers for db
```shell
poetry add sqlmodel psycopg
```

add drivers (one line command) mac
```shell
poetry add fastapi sqlmodel uvicorn\[standard\] psycopg 
```

add drivers (one line command) window
```shell
poetry add fastapi uvicorn[standard] sqlmodel psycopg 
```

run poetry app
```shell
poetry run uvicorn folder_name.file_name:app --port 8000 --reload
```

```shell
poetry run uvicorn app.main:app --reload
```

### Contecting with db

#### DATABASE_URL

```bash
connection_string = str(DATABASE_URL).replace("postgresql", "postgresql+psycopg")
``` 

This code modifies the DATABASE_URL so it can use the psycopg driver when connecting to a PostgreSQL database:

**str(DATABASE_URL):** Converts DATABASE_URL into a string representation, which is necessary for the replacement to be performed.

**.replace("postgresql", "postgresql+psycopg"):** Changes "postgresql" to "postgresql+psycopg" in the connection string. This ensures that SQLAlchemy knows to use the psycopg driver to connect to the PostgreSQL database.

**psycopg** driver is a popular and efficient library for interacting with PostgreSQL databases in Python

#### create a connection to the database

```bash
engine = create_engine(connection_string, connect_args={}, pool_recycle=300)
``` 

**create_engine()** SQLModel Function (create a connection to the database)

**Detail Description**

**connection_string:** Specifies the database URL (e.g., the type of database and its location).

**connect_args={}:** Additional arguments for the connection (often used for settings specific to the type of database).

**pool_recycle=300:** Prevents stale connections by recycling (re-establishing) them every 300 seconds to avoid issues like timeout.

####  Create all tables defined in the model
```bash
SQLModel.metadata.create_all(engine)
``` 

**SQLModel.metadata.create_all()**

**.metadata:** attribute keeps track of all the models (tables)

**.create_all():** Uses .metadata to create the tables in your database

**.engine:** SQLAlchemy database engine that points to your database.

**Detail Description**

SQLModel: It’s a library built on top of SQLAlchemy and Pydantic that simplifies working with SQL databases in Python, commonly used with FastAPI for defining database models.

.metadata: This attribute of SQLModel contains metadata about all the defined tables, such as table names and their columns. It acts as a registry for your models.

.create_all(): This method, when called, uses the metadata to generate SQL commands that create the necessary tables in the connected database. Essentially, it will ensure all your defined models have corresponding tables.

### Get Form Data

**creates a new User object using the details provided in form_data.**

```bash
User(**form_data.model_dump())
``` 

form_data.model_dump():- return a dictionary of the data stored in form_data

(**form_data.model_dump()) :- unpacks the form_data dictionary into keyword arguments

**Note**  ** (double asterisk): unpacks a dictionary into keyword arguments.

**Detail Description**

**1- Pydantic Model:** User instance (form_data) holds user details.

**2- Convert to Dictionary:** form_data.model_dump() converts the instance to a dictionary.

**3- Dictionary Unpacking:** **form_data.model_dump() unpacks the dictionary into keyword arguments.

**4- Create User Object:** User(**form_data.model_dump()) creates a new User object with the provided details.

**model_dump()** method in Pydantic :- converts a model instance into a dictionary with the model's attribute names as keys and their corresponding values.

### Update Form Data

```bash
query = select(User).where(User.user_id == selected_id)
``` 
select(User): Specifies that you want to select data from the User table.

.where(User.user_id == selected_id): Adds a condition to filter the results to only include rows where user_id matches selected_id.

Executing Raw SQL :- session.execute() to run raw SQL queries


### Tutorials

[First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)

[Create a Table with SQLModel - Use the Engine](https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#last-review)


[Can Pydantic model_dump() return exact type?](https://stackoverflow.com/questions/77476105/can-pydantic-model-dump-return-exact-type)
<<<<<<< HEAD
=======


**==========================================================**

## Tutorials Details  check

**lifespan**
-lifespan function provide by FastAPI (create db table at start of program)
-function, before the yield, will be executed before the application starts.
-it create table only one-time, if table is already created, won't create again
Create FastAPI instance
app = FastAPI(lifespan= create_db_and_tables)

**session**
-create object of session and pass engine in it and return in local-variable session
-get-session is created on server.  (engine give db connectivity) 
def get_session():
    with Session(engine) as session:
        yield session


**SQLModel** (ORM)

we use other methods
[SQLModel : Delete Data - DELETE](https://sqlmodel.tiangolo.com/tutorial/delete/#review-the-code)


**pytest cache directory**

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.


[How to re-run failed tests and maintain state between test runs](https://docs.pytest.org/en/stable/how-to/cache.html)

[OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/?h=jwt)


**JWT means "JSON Web Tokens"** (It is not encrypted), Install python-jose

- jwt token decode  # Decoding the token
-decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
>>>>>>> be1e33e (product_service)

