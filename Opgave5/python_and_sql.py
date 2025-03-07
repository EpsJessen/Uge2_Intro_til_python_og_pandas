import pandas as pd
import getpass
import matplotlib.pyplot as plt
import os.path
from mysql.connector import errorcode
from sqlalchemy import create_engine

sql_path = os.path.join("Opgave5", "northwind.sql")
db_path = os.path.join("Opgave5", "northwind.db")

print("You should have mySQL workbench serving the database at localhost:3306")

user = input("Please enter your username: ")
password = getpass.getpass("Please enter your password: ")


connection_string = f"mysql+mysqlconnector://{user}:{password}@localhost:3306/northwind"
engine = create_engine(connection_string)

with engine.connect() as connection:

    query = "select orders.orderid, orders.shipcountry, orderdetails.discount, products.unitprice, orderdetails.quantity "
    query += "from orders "
    query += "inner join orderdetails on orders.orderid = orderdetails.orderid "
    query += "inner join products on orderdetails.productid = products.productid;"
    nw_full_orders = pd.read_sql(query, connection)
    print(nw_full_orders.head(10))

