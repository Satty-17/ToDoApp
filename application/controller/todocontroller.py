from flask import abort, redirect, render_template, flash, request
from application import app
from application.forms import TodoForm
from application.service.todoservice import TodoService
from application import schemas

@app.route("/")
def get_todos():
    try:
        todos = TodoService.get_all_todos()
        return render_template("view_todos.html", title="Layout page", todos=todos)
    except Exception as e:
        flash(f"Error fetching todos: {str(e)}", "danger")
        return redirect("/")

@app.route("/add_todo", methods=["POST", "GET"])
def add_todo():
    try:
        if request.method == "POST":
            TodoService.add_todo(request)
            flash("Todo successfully added", "success")
            return redirect("/")
        else:
            form = TodoForm()
        return render_template("add_todo.html", form=form)
    except Exception as e:
        flash(f"Error adding todo: {str(e)}", "danger")
        return redirect("/")

@app.route("/update_todo/<id>", methods=["POST", "GET"])
def update_todo(id):
    try:
        if request.method == "POST":
            TodoService.update_todo(id, request)
            flash("Todo successfully updated", "success")
            return redirect("/")
        else:
            form = TodoForm()
            todo = TodoService.get_todo_by_id(id)
            if not todo:
                abort(404)  # Return a 404 error if the todo is not found

            form.name.data = todo.get("name", None)
            form.description.data = todo.get("description", None)
            form.completed.data = todo.get("completed", None)

        return render_template("add_todo.html", form=form)
    except Exception as e:
        flash(f"Error updating todo: {str(e)}", "danger")
        return redirect("/")

@app.route("/delete_todo/<id>")
def delete_todo(id):
    try:
        TodoService.delete_todo(id)
        flash("Todo deleted", "success")
        return redirect("/")
    except Exception as e:
        flash(f"Error deleting todo: {str(e)}", "danger")
        return redirect("/")
