from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash
from .CostCalculation import costCalculation

from .forms import *
import numpy as np
from .resv_table_numpy import createChart


#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():

    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")

    return render_template("options.html", title="Choose Option", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    err = None
    chart = None
    cost = None
    form = AdminLoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form['username']
            password = request.form['password']

            success = False
            with open('passcodes.txt', 'r') as f:

                for line in f:
                    passcodes = line.split(',')
                    un = passcodes[0]
                    pw = passcodes[1].strip()

                    if (un == username and pw == password):
                        print("You're logged in.")
                        success = True
                        break

            if (success == False):
                err = "Bad username/password combination. Try Again"
            else:
                #TODO: Chart needs to be set to seating chart here.
                # chart = []
                # chart.append(["X"] * 4)
                # chart.append(["O"] * 4)
                # chart.append(["O"] * 4)
                # chart.append(["O"] * 4)
                # chart.append(["O"] * 4)
                # chart.append(["O"] * 4)
                # chart.append(["O"] * 4)
                # chart.append(["O"] * 4)
                # chart.append(["O"] * 4)
                # chart.append(["O"] * 4)
                # chart.append(["O"] * 4)
                # chart.append(["O"] * 4)

                initialChart = createChart()

                cost = costCalculation(initialChart)

                chart = initialChart.tolist()

            return render_template("admin.html", err=err, chart=chart, cost=cost, form=form, template="form-template")

    return render_template("admin.html", title="Admin Login", form=form, template="form-template")

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()

    return render_template("reservations.html", title="Reservations", form=form, template="form-template")
