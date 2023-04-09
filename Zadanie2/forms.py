import json
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField

class CostForm(FlaskForm):
    title   = StringField()
    description = TextAreaField()
    done = BooleanField()
