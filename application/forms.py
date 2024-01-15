from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
class TodoForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    completed = SelectField("Completed", choices=[("TODO", "TODO"),("COMPLETED", "COMPLETED"),("IN PROGRESS", "IN PROGRESS")], validators = [DataRequired()])
    submit = SubmitField("Add Todo")