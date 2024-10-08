from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Optional, Annotated

from app.settings import DB_URL

class ProductModel(SQLModel):
    product_name: str
    product_desc: str

class Product(ProductModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

# Set up the database connection
connection_string = str(DB_URL).replace(
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

# function, before the yield, will be executed before the application starts.
# create session to get memory space in db
def get_session():
    with Session(engine) as session:
        yield session

# Dependency injection to get a session
DB_Session = Annotated[Session, Depends(get_session)]

# lifespan function provide by FastAPI (create db table at start of program)
# it create table only one-time, if table is already created, won't create again
# Create FastAPI instance
async def life_span(app: FastAPI):
    print("Creating tables during lifespan startup... ")
    await create_db_and_tables()  # Properly await the table creation
    yield  # Lifespan generator is working correctly


app = FastAPI(lifespan=life_span, title='Product API')

@app.get('/')
def get_root_route():
    return "Product Service"

# Function to add a product into the database
def add_product_into_db(form_data: ProductModel, session: Session):
    product = Product(**form_data.model_dump())  # Use dict() to convert Pydantic model to dict
    
    # Add the product to the session
    session.add(product)
    # Commit the session to save the product to the database
    session.commit()
    # Refresh the session to retrieve the new product data
    session.refresh(product)
    print("New product added:", product)
    return product

# POST route to add a new product
@app.post('/api/add_product')
def add_product(new_product: ProductModel, session: DB_Session):
    added_product = add_product_into_db(new_product, session)  # Call function to add product
    print("Add product route ...", added_product)
    return added_product







