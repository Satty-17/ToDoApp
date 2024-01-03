from jsonschema import validate, ValidationError
from datetime import datetime
from flask_pymongo import PyMongo
from application import db
from bson import ObjectId

mongo = PyMongo()

class TodoModel:
    SCHEMA = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "description": {"type": "string"},
            "completed": {"type": "string"}
        },
        "required": ["name", "description", "completed"],
    }

    @staticmethod
    def validate_todo(todo):
        try:
            todo["date_created"] = todo["date_created"]
            validate(instance=todo, schema=TodoModel.SCHEMA)
            return True
        except ValidationError as e:
            print(e)
            return False

    @staticmethod
    def get_all_todos():
        try:
            todos = db.todo_flask.find().sort("date_created", -1)
            return [dict(todo, _id=str(todo["_id"])) for todo in todos]
        except Exception as e:
            print(f"Error fetching todos: {e}")
            return []

    @staticmethod
    def add_todo(todo_name, todo_description, completed):
        try:
            todo = {
                "name": todo_name,
                "description": todo_description,
                "completed": completed,
                "date_created": datetime.utcnow(),
            }

            if TodoModel.validate_todo(todo):
                db.todo_flask.insert_one(todo)
                return True
            else:
                return False
        except Exception as e:
            print(f"Error adding todo: {e}")
            return False

    @staticmethod
    def update_todo(todo_id, todo_name, todo_description, completed):
        try:
            todo = {
                "name": todo_name,
                "description": todo_description,
                "completed": completed,
                "date_created": datetime.utcnow(),
            }

            if TodoModel.validate_todo(todo):
                db.todo_flask.find_one_and_update(
                    {"_id": ObjectId(todo_id)},
                    {"$set": {
                        "name": todo_name,
                        "description": todo_description,
                        "completed": completed,
                        "date_created": datetime.utcnow()
                    }}
                )
                return True
            else:
                return False
        except Exception as e:
            print(f"Error updating todo: {e}")
            return False

    @staticmethod
    def get_todo_by_id(todo_id):
        try:
            return db.todo_flask.find_one({"_id": ObjectId(todo_id)})
        except Exception as e:
            print(f"Error getting todo by ID: {e}")
            return None

    @staticmethod
    def delete_todo(todo_id):
        try:
            db.todo_flask.find_one_and_delete({"_id": ObjectId(todo_id)})
            return True
        except Exception as e:
            print(f"Error deleting todo: {e}")
            return False
