from application import app
from flask import redirect, render_template, flash, request, url_for
from .forms import TodoForm
from flask.templating import render_template_string
from werkzeug.datastructures import RequestCacheControl
from datetime import datetime
from application import db
import pytz
from bson import ObjectId

# Set the Indian Standard Time timezone


@app.route("/")
def get_todos():
    todos = []
    for todo in db.todo_flask.find().sort("date_created", -1):
        todo["_id"] = str(todo["_id"])

        

        todos.append(todo)
    return render_template("view_todos.html", title="Layout page", todos=todos)

@app.route("/add_todo", methods=["POST", "GET"])
def add_todo():
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        # Get the current time in IST
        

        db.todo_flask.insert_one({
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "date_created": datetime.utcnow()  # Store the date in IST
        })

        flash("Task Successfully added", "success")
        return redirect("/")
    else:
        form = TodoForm()
    return render_template("add_todo.html", form=form)

@app.route("/update_todo/<id>", methods = ["POST", "GET"])
def update_todo(id):
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        db.todo_flask.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "date_created": datetime.utcnow()
        }})

        flash("Todo successfully updated", "success")
        return redirect("/")

    else:
        form = TodoForm()
        todo = db.todo_flask.find_one_or_404({"_id": ObjectId(id)})
        form.name.data = todo.get("name", None)
        form.description.data = todo.get("description", None)
        form.completed.data = todo.get("completed", None)
    
    return render_template("add_todo.html", form = form)