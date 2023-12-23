from flask import Flask
from flask_pymongo import PyMongo
from urllib.parse import quote_plus

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
username = "Satvik17"
password = "chhikara@010"
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)
uri = f"mongodb+srv://{escaped_username}:{escaped_password}@todoappcluster.xiwjboc.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
print(client.list_database_names())
db=client["todo"]
app = Flask(__name__)
app.config["SECRET_KEY"] = "5375a1a9dfb22bc3fbeb00ef4680d078fe46a38e"


from application import routes
