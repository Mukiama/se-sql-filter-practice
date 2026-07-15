import pandas as pd
import sqlite3

conn = sqlite3.connect('data.sqlite')

employees = pd.read_sql("""
SELECT *
  FROM employees;
""", conn)

# print(employees)

Leslie = pd.read_sql("""
SELECT firstName, lastName, jobTitle
  FROM employees
   WHERE firstName ="Leslie";
""", conn)

# print(Leslie)

name_length = pd.read_sql("""
SELECT *, length(lastName) AS name_length
 FROM employees
WHERE name_length < 5;
""", conn)

# print(name_length)

order_details = pd.read_sql("""
SELECT *
  FROM orderDetails;
""", conn)

# print(order_details)

rounded_prices = pd.read_sql("""
SELECT *, CAST(ROUND(priceEach) AS INTEGER) AS rounded_price
  FROM orderDetails;
""", conn)

# print(rounded_prices)

orders_placed_in_2005 = pd.read_sql("""
SELECT *, strftime("%Y", orderDate) AS year
 FROM orders
WHERE year = "2005";
""", conn)

# print(orders_placed_in_2005)

sales_as_jobtitle = pd.read_sql("""
SELECT *
 FROM employees
WHERE jobTitle LIKE "Sale%";
""", conn)

# print(sales_as_jobtitle)

count_items_priced_200_and_above = pd.read_sql("""
SELECT COUNT(priceEach)
 FROM orderDetails
WHERE priceEach >= 200;
""", conn)

print(count_items_priced_200_and_above)
