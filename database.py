from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql://postgres:jaydave@localhost:5432/sales"
)

engine = create_engine(
    DATABASE_URL
)

print("Database connection created")