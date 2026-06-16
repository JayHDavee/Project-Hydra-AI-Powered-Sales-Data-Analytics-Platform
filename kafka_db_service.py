from sqlalchemy import text
from database import engine


def insert_order(order):

    with engine.begin() as conn:

        conn.execute(
            text(
                """
                INSERT INTO orders
                (
                    orderid,
                    customerid,
                    productid,
                    quantity,
                    orderdate,
                    status
                )
                VALUES
                (
                    :orderid,
                    :customerid,
                    :productid,
                    :quantity,
                    :orderdate,
                    :status
                )
                """
            ),
            order
        )

    print("Inserted into Orders")