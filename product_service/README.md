# Online Mart - Product Service

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
**======================== ** ** ========================**

### Contecting with db

.env  (Write secret credential.)

```bash
DATABASE_URL =
```

**Note:-** When copying the database URL (DB_URL), ensure that only the owner has access to add, update, and delete data. Developers should have limited write access.

#### DATABASE_URL

setting.py
```bash
from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()  

DATABASE_URL = config("DATABASE_URL", cast=Secret)
```

**======================== ** ** ========================**

### Contection String

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

### Session

```bash
def get_session():
    with Session(engine) as session:
        yield session
``` 

This function creates a session object using the provided engine for database connectivity, and it yields this session. It ensures that the session is properly created and closed after use. 

**- with** statement ensures that resources are properly managed, like automatically closing the session after it's used.

**- yield** allows a function to return a value and then pause its execution, resuming right where it left off the next time it’s called. This is what makes a generator function. It’s perfect for situations where you want to iterate through a sequence without storing the entire thing in memory

The code in the function before yield will be executed each time the generator is called.

### Lifespan

Lifespan function provided by FastAPI (creates DB table at program startup)
It creates the table only once; if the table already exists, it won't create it again

```bash
async def life_span(app: FastAPI):
    print("Creating tables during lifespan startup...")
    await create_db_and_tables()  # Properly await table creation
    yield  # Lifespan generator is working correctly
``` 

### Create FastAPI instance

```bash
app = FastAPI(lifespan=life_span, title='Fast API')
``` 

**======================== ** ** ========================**

### Retrive Data

```bash
statement = select(User)
user_list = session.exec(statement).all()
```

**select(User)** creates a query to select all records from the User table.

**user_list = session.exec(statement).all()** executes the query and retrieves all results as a list by calling .all()

Note :-  **.all()** is used on the result of session.exec(statement) to get a list of all rows immediately, instead of returning an iterable.

### Create Data 

**creates a new user object using the details provided in form_data.**

#### Get Form Data

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

### Update Record 

#### Update Form Data

```bash
statement = select(User).where(User.user_id == selected_id)
selected_user = session.exec(statement).first()
``` 

**select(User)**: Specifies that you want to select data from the User table.

**.where()** filter rows 

**.where(User.user_id == selected_id)**: Adds a condition to filter the results to only include rows where user_id matches selected_id.

Executing Raw SQL :- **session.exec()** to run raw SQL queries

### Delete Record

```bash
session.get(User, delete_id)
``` 

**session.get(User, delete_id)** retrieves a specific record from the User table where the primary key matches the value of **delete_id**. If a matching record is found, it returns the corresponding User object; otherwise, it returns None.

**get()** is a versatile method that enhances both dictionary manipulations and HTTP requests in Python.

**======================== ** ** ========================**

### Tutorials

[First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)

[Create a Table with SQLModel - Use the Engine](https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#last-review)

[Read Data - SELECT](https://sqlmodel.tiangolo.com/tutorial/select/#review-the-code)

[Can Pydantic model_dump() return exact type?](https://stackoverflow.com/questions/77476105/can-pydantic-model-dump-return-exact-type)

[Models with Relationships in FastAPI](https://sqlmodel.tiangolo.com/tutorial/fastapi/relationships/)

[Filter Data - WHERE](https://sqlmodel.tiangolo.com/tutorial/where/)

[Update Data - UPDATE](https://sqlmodel.tiangolo.com/tutorial/update/#read-from-the-database)


[SQLModel : Delete Data - DELETE](https://sqlmodel.tiangolo.com/tutorial/delete/#review-the-code)

[Delete Data - DELETE](https://sqlmodel.tiangolo.com/tutorial/delete/)

**======================== ** ** ========================**

## Tutorials Details  

**SQLModel** (ORM)

[How to re-run failed tests and maintain state between test runs](https://docs.pytest.org/en/stable/how-to/cache.html)

[OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/?h=jwt)


**JWT means "JSON Web Tokens"** (It is not encrypted), Install python-jose

- jwt token decode  # Decoding the token
-decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

**======================== ** ** ========================**
