from flask import jsonify, flash
from application.models.todomodel import TodoModel
from application.forms import TodoForm

class TodoService:

    @staticmethod
    def get_all_todos():
        try:
            todos = TodoModel.get_all_todos()
            return todos
        except Exception as e:
            return jsonify({"error": str(e)})

    @staticmethod
    def add_todo(request):
        try:
            form = TodoForm(request.form)
            todo_name = form.name.data
            todo_description = form.description.data
            completed = form.completed.data
            TodoModel.add_todo(todo_name, todo_description, completed)
            flash("Task Successfully added", "success")
            return jsonify({"message": "Task Successfully added"})
        except Exception as e:
            return jsonify({"error": str(e)})

    @staticmethod
    def update_todo(todo_id, request):
        try:
            form = TodoForm(request.form)
            todo_name = form.name.data
            todo_description = form.description.data
            completed = form.completed.data
            TodoModel.update_todo(todo_id, todo_name, todo_description, completed)
            return jsonify({"message": "Todo successfully updated"})
        except Exception as e:
            return jsonify({"error": str(e)})

    @staticmethod
    def get_todo_by_id(todo_id):
        try:
            return TodoModel.get_todo_by_id(todo_id)
        except Exception as e:
            return jsonify({"error": str(e)})

    @staticmethod
    def delete_todo(todo_id):
        try:
            TodoModel.delete_todo(todo_id)
            return jsonify({"message": "Todo deleted"})
        except Exception as e:
            return jsonify({"error": str(e)})
