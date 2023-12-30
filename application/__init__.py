from flask import Flask
from flask_pymongo import PyMongo
from urllib.parse import quote_plus
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv


load_dotenv()


username = os.getenv("MONGODB_USER")
password = os.getenv("MONGODB_PASSWORD")
cluster = os.getenv("MONGODB_CLUSTER")
database = os.getenv("MONGODB_DATABASE")
secret_key = os.getenv("SECRET_KEY")


escaped_username = quote_plus(username)
escaped_password = quote_plus(password)
uri = f"mongodb+srv://{escaped_username}:{escaped_password}@{cluster}/?retryWrites=true&w=majority"


client = MongoClient(uri, server_api=ServerApi('1'))


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

print(client.list_database_names())
db = client[database]

app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key

from application import routes
