# online_mart_class

<<<<<<< HEAD
=======
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

>>>>>>> be1e33e (product_service)
**Methods HTTP (Hypertext Transfer Protocol)**

GET: Retrieves data from a server.

POST: Sends data to the server to create a new resource. 

PUT: Updates or replaces an existing resource on the server.

DELETE: Removes a resource from the server.

PATCH: Applies partial modifications to a resource.


## Tutorials

[Simple Hero API with FastAPI](https://sqlmodel.tiangolo.com/tutorial/fastapi/simple-hero-api/)

[Using Dataclasses](https://fastapi.tiangolo.com/advanced/dataclasses/)

[Read Data - SELECT](https://sqlmodel.tiangolo.com/tutorial/select/#create-a-select-statement)

[Why Aren't We Getting More Data](https://sqlmodel.tiangolo.com/tutorial/fastapi/relationships/#why-arent-we-getting-more-data)

[Models with Relationships in FastAPI](https://sqlmodel.tiangolo.com/tutorial/fastapi/relationships/)

[Filter Data - WHERE](https://sqlmodel.tiangolo.com/tutorial/where/)

[Update Data - UPDATE](https://sqlmodel.tiangolo.com/tutorial/update/#read-from-the-database)

[Delete Data - DELETE](https://sqlmodel.tiangolo.com/tutorial/delete/)
<<<<<<< HEAD
=======

**Advanced Topics**

[Hash and verify the passwords](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/?h=jwt#hash-and-verify-the-passwords)

[Default values](https://python.useinstructor.com/concepts/fields/)

[Fastapi-mail](https://sabuhish.github.io/fastapi-mail/)

[Test Applications with FastAPI and SQLModel](https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/?h=test#__code_5_annotation_4)

**Docker**

[Profiles](https://docs.docker.com/reference/compose-file/profiles/)

[Using profiles with Compose](https://docs.docker.com/compose/how-tos/profiles/)



>>>>>>> be1e33e (product_service)
