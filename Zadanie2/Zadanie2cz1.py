from flask import Flask, request, render_template, redirect, url_for
import json
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from forms import CostForm
from models import costs

import flask_wtf
flask_wtf.__version__

f=flask_wtf.__version__
print(f)

app = Flask(__name__)
app.config["SECRET_KEY"] = "kjgfdzs"

@app.route("/home/", methods=["GET", "POST"])
def home_costs():
    form = CostForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            costs.create(form.data)
            costs.save_all()
        return redirect(url_for("home_costs"))

    return render_template("home.html", form=form, costs=costs.all(), error=error)


@app.route("/home/<int:cost_id>", methods=["GET", "POST"])
def home_costs_details(cost_id):
    cost = costs.get(cost_id - 1)
    form = CostForm(data=cost)
    if request.method == "POST":
        if form.validate_on_submit():
            costs.update(cost_id - 1, form.data)
        return redirect(url_for("home_costs"))
    return render_template("cost_id.html", form=form, cost_id=cost_id)


if __name__ == "__main__":
    app.run(debug=True)