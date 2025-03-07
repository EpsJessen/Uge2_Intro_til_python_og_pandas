import pandas as pd
import getpass
import matplotlib.pyplot as plt
import os.path
from mysql.connector import errorcode
from sqlalchemy import create_engine

def plot_path(name:str) -> str:
    return os.path.join("Opgave5", name)

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
    #print(nw_full_orders.head(10))

    #Add column for the total price of an order
    nw_full_orders["totalprice"] = nw_full_orders.unitprice * nw_full_orders.quantity * (1-nw_full_orders.discount)
    
    ship_country_group = nw_full_orders.groupby(["shipcountry"])
    mean_price_by_country = ship_country_group[["totalprice"]].mean()
    mean_price_by_country.plot(kind = "bar", legend=False, title="Mean spending per order by country")
    plt.tight_layout()
    name = plot_path("country_mean_spending.png")
    plt.savefig(name)

    total_price_by_country = ship_country_group[["totalprice"]].sum()
    total_price_by_country.plot(kind = "bar", title="Total spending by country", legend=False)
    
    name = plot_path("country_total_spending.png")
    plt.savefig(name)

    total_price_by_country = ship_country_group[["totalprice"]].count()
    total_price_by_country.plot(kind="bar", legend=False, title="Total orders per country")
    name = plot_path("country_total_orders.png")
    plt.savefig(name)

    query = "select orderdate, shippeddate, requireddate, employeeid "
    query += "from orders"
    nw_orders_dates = pd.read_sql(query, connection)
    nw_orders_dates["fulfilmenttime"] = (nw_orders_dates.shippeddate - nw_orders_dates.orderdate).dt.days
    nw_orders_dates["delay"] = nw_orders_dates.requireddate < nw_orders_dates.shippeddate
    #print(nw_orders_dates.head(10))

    time_employee_group = nw_orders_dates.groupby(["employeeid"])
    mean_time_by_employee = time_employee_group[["fulfilmenttime"]].mean()
    #print(mean_time_by_employee.head(10))
    mean_time_by_employee.plot(kind = "bar", legend=False, title="Mean time per order by employee")
    name = plot_path("employee_mean_fulfilment.png")
    plt.savefig(name)

    frac_delay_by_employee = time_employee_group[["delay"]].mean()
    #print(frac_delay_by_employee.head(10))
    frac_delay_by_employee.plot(kind = "bar", legend=False, title="Fraction delayed orders by employee")
    name = plot_path("employee_fraction_delay.png")
    plt.savefig(name)

    max_time_by_employee = time_employee_group[["fulfilmenttime"]].max()
    #print(max_time_by_employee.head(10))
    max_time_by_employee.plot(kind = "bar", legend=False, title="Worst delivery time by employee")
    name = plot_path("employee_max_fulfilment.png")
    plt.savefig(name)
