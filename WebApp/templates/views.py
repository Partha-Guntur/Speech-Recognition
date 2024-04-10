from flask import Blueprint, render_template, request, redirect
import csv
import pandas as pd
views = Blueprint('views', __name__)


@views.route('/', methods=["GET", "POST"])
def login():
    return render_template("main.html")

# @views.route('/reg_patients')
# def reg_patients():
#     email = request.form.get("email")
#     emails.append(email)
#     name.append(emails[1].split('@'))
#     return render_template('/reg_patients.html', email = name[0][0])

# @views.route('/reg_patients', methods=["GET", "POST"])
# def registered():
#     firstName = request.form.get("firstName")
#     lastName = request.form.get("lastName")
#     gender = request.form.get("gender")
#     description = request.form.get("description")
#     name = (f"{firstName} {lastName}")
#     patients.append(f"Name: {name} \nGender:{gender} \nDescription:{description}")
#     file = open("patient_details.csv" ,"a")
#     writer = csv.writer(file)
#     writer.writerow((name, gender, description))
#     file.close()
#     return redirect('/reg_patients')
