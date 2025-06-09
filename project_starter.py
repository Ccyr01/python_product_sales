# TODO 1: Import the necessary libraries (csv, datetime)
import csv
import datetime

# TODO 2: Define the product_data dictionary with product IDs, names, and unit prices
product_data = {
    "P001": ["Wireless Headphones", 100],
    "P002": ["Laptop Backpack", 60],
    "P003": ["Bluetooth Speaker", 50],
    "P004": ["USB Flash Drive", 20],
    "P005": ["Mobile Phone Case", 15],
    "P006": ["Wireless Mouse", 30],
    "P007": ["Laptop Stand", 40],
    "P008": ["HDMI Cable", 15],
    "P009": ["Smartphone", 600],
    "P010": ["External Hard Drive", 100],
}

# TODO 3: Read the "product_sales.txt" file and store the product IDs in a list
# Hint: Use the built-in 'open' function to open the file, and the 'readlines' method to read its lines into a list.
products = []

with open("product_sales.txt", "r") as file:
    product_ids = file.readlines()
    current_date = datetime.date.today()

    for sale_id, product_id in enumerate(product_ids):
        product_id = product_id.strip()
        product_name = product_data[product_id][0]
        product_price = product_data[product_id][1]
        row = [current_date, sale_id, product_id, product_name, product_price]
        products.append(row)

with open("product_sales.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["current_date", "sale_id", "product_id", "product_name", "product_price"])
    csv_writer.writerows(products)