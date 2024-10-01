# online mart - user service

poetry —-version

**Create Poetry Project**

create new project
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

generate a random string of bytes in hexadecimal format
```bash
openssl rand -hex 32
``` 

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

**Detail**

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

**Detail**

SQLModel: It’s a library built on top of SQLAlchemy and Pydantic that simplifies working with SQL databases in Python, commonly used with FastAPI for defining database models.

.metadata: This attribute of SQLModel contains metadata about all the defined tables, such as table names and their columns. It acts as a registry for your models.

.create_all(): This method, when called, uses the metadata to generate SQL commands that create the necessary tables in the connected database. Essentially, it will ensure all your defined models have corresponding tables.


####  User(**form_data.model_dump())

**1- Pydantic Model:** User instance (form_data) holds user details.

**2- Convert to Dictionary:** form_data.model_dump() converts the instance to a dictionary.

**3- Dictionary Unpacking:** **form_data.model_dump() unpacks the dictionary into keyword arguments.

**4- Create User Object:** User(**form_data.model_dump(), user_password=hashed_password) creates a new User object with the provided details and the hashed password.

**model_dump()** method in Pydantic :- converts a model instance into a dictionary with the model's attribute names as keys and their corresponding values.


**Tutorials**

[First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)

[Create a Table with SQLModel - Use the Engine](https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#last-review)


[Can Pydantic model_dump() return exact type?](https://stackoverflow.com/questions/77476105/can-pydantic-model-dump-return-exact-type)

