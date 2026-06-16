from urllib import response

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from database import engine
import pandas as pd
from ai_sql_generator import generate_sql
from sqlalchemy import text
from schema_service import get_schema
from query_service import execute_query
from kafka_producer import (
    send_sale_event
)
from csv_service import get_csv_summary

app = FastAPI(
    title="AI Data Engineering Platform"
)

@app.get("/")
def home():

    return {
        "message":
            "AI Data Engineering Platform"
    }

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    table_name = (
        file.filename
        .replace(".csv", "")
        .lower()
    )

    df.columns = (
    df.columns
      .str.strip()
      .str.lower()
)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    summary = get_csv_summary(df)

    return {
        "message": "CSV stored successfully",
        "table_name": table_name,
        **summary
    }

@app.get("/datasets")
def list_datasets():

    with engine.connect() as conn:
        query = text("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema='public'
        """)

        result = conn.execute(query)

        tables = [row[0] for row in result]

    return {
        "datasets": tables
    }

@app.get("/dataset/{table_name}")
def get_dataset_preview(
    table_name: str
):

    query = f"""
        SELECT *
        FROM {table_name}
        LIMIT 10
    """

    df = pd.read_sql(
        query,
        engine
    )

    return {
        "rows": df.to_dict(
            orient="records"
        )
    }

@app.get("/dataset/{table_name}/summary")
def get_dataset_summary(
    table_name: str
):

    query = f"""
        SELECT * FROM {table_name}
    """

    df = pd.read_sql(
        query,
        engine
    )

    summary = get_csv_summary(df)

    return {
        "table_name": table_name,
        **summary
    }

@app.post("/query")
def query_database(
    request: dict
):

    question = request["question"]

    sql_query = generate_sql(
        question
    ).replace("```sql", "").replace("```", "").strip()

    print(f'type(sql_query)): {type(sql_query)}')

    print(f"Generated SQL: {sql_query}")

    if sql_query is None:

        return {
            "error":
            "Question not supported"
        }

    df = pd.read_sql(
        text(sql_query),
        engine
    )

    query_result = execute_query(
        sql_query
    )

    return {
        "question": question,
        "generated_sql": sql_query,
        "data": query_result
    }

@app.get("/schema")
def schema():

    return get_schema()

@app.post("/sale")
def create_sale(
    sale: dict
):

    send_sale_event(
        sale
    )

    return {
        "message":
        "Sale event sent to Kafka"
    }
