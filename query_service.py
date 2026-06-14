import pandas as pd
from sqlalchemy import text
from database import engine


def execute_query(sql_query):

    try:

        df = pd.read_sql(
            text(sql_query),
            engine
        )

        return {
            "success": True,
            "results":
                df.to_dict(
                    orient="records"
                )
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }
        