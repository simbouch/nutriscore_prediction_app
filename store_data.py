from pymongo import MongoClient
import first

def connect_to_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['open_food_facts']  # Create or connect to a database named 'open_food_facts'
    collection = db['nutri_score']   # Create or connect to a collection named 'nutri_score'
    return collection

def store_data_in_mongodb(data):
    collection = connect_to_mongodb()
    collection.insert_one(data)  # Insert the product data into the MongoDB collection

data_list = first.fetch_all_products(1000)
if data_list:
    for data in data_list:
        store_data_in_mongodb(data)
        print("Data stored successfully.")
