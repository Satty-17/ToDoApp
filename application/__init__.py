from flask import Flask
from flask_pymongo import PyMongo
from urllib.parse import quote_plus
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

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

# print(client.list_database_names())
db = client[database]

app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key

from .controller import todocontroller

# complete_task= db.todo_flask.find({ "completed": "True" })
# for task in complete_task:
#     print(task["name"])

# most_recent_tasks = db.todo_flask.find().sort("date_created").limit(5)
# for task in most_recent_tasks:
#     print(task["name"])
# now = datetime.now()
# yesterday = now - timedelta(days=1)
# print(yesterday)
# pending_tasks = list(db.todo_flask.find({
#     "completed": "False",
#     "date_created": {"$lt": now, "$gt": yesterday}
# }))
# print("Tasks pending since 24 hrs:")
# for task in pending_tasks:
#     print(task["name"])




