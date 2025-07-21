from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # load variables from .env

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["ecommerce"]

