from pymongo import MongoClient
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["publicwww"]

def load(collection_name, records):
    try:
        if not records:
            logging.warning(f"No records to load for {collection_name}")
            return
        collection = db[collection_name.replace("/", "_")]
        collection.insert_many(records)
        logging.info(f"Inserted {len(records)} records into {collection_name}")
    except Exception as e:
        logging.error(f"Error loading {collection_name}: {e}")

def load_list_details(records, extract_list_detail):
    for record in records:
        list_id = record.get("id")
        if not list_id:
            continue
        detail = extract_list_detail(list_id)
        if detail:
            load("list_details", [detail])
