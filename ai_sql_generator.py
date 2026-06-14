import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_sql(
    question,
):

    prompt = f"""
You are a PostgreSQL expert.

Database Schema:
"customers":["customerid","customername","email","phone","state","city","joindate"],
"orders":["orderid","customerid","productid","quantity","orderdate","status"],
"products":["productid","productname","category","price"],
"sales_data":["orderid","orderdate","customerid","customername","state","city","product","category","quantity","unitprice","revenue"]

Generate ONLY PostgreSQL SQL.

If the question asks for:
- total revenue by state -> use SUM() and GROUP BY
- top customers -> use ORDER BY and LIMIT
- counts -> use COUNT()

Return SQL query only, not with any other special characters or words.
Remove ```sql and ``` if they are present.

Question:
{question}
"""

    response = model.generate_content(
        prompt
    )

    return response.text.strip()
