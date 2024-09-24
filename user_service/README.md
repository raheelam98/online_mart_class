# online mart - user service

## Create Poetry Project 

create new project
```bash
poetry —-version
poetry new project_name 
d project_name
```

add drivers
```shell
poetry add fastapi uvicorn\[standard\] 
```

add drivers for db
```shell
poetry add sqlmodel psycopg
```

add drivers (one line command)
```shell
poetry add fastapi sqlmodel uvicorn\[standard\] psycopg 
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

**Tutorials**

[Simple Hero API with FastAPI](https://sqlmodel.tiangolo.com/tutorial/fastapi/simple-hero-api/)

[Using Dataclasses](https://fastapi.tiangolo.com/advanced/dataclasses/)

[Read Data - SELECT](https://sqlmodel.tiangolo.com/tutorial/select/#create-a-select-statement)