from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash
from .CostCalculation import costCalculation
from .forms import *
import numpy as np
from .resv_table_numpy import createChart
from .presentChart import presentChart
from .reservation import addRes
from .confirmationNumber import createConfirmationNum

initialChart = createChart()

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
                cost = costCalculation(initialChart)

                chart = presentChart(initialChart)

            return render_template("admin.html", err=err, chart=chart, cost=cost, form=form, template="form-template")

    return render_template("admin.html", title="Admin Login", form=form, template="form-template")

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():
    err=None
    form = ReservationForm()
    if request.method == 'POST' and form.validate_on_submit():
        row = request.form['row']
        column = request.form['seat']
        firstName = request.form['first_name']
        it4320String = "INFOTC4320"

        if(initialChart[int(row)-1, int(column)-1] == "O"):
            initialChart[int(row)-1, int(column)-1] = "X"

            confirmationNumber = createConfirmationNum(firstName, it4320String)
            addRes(firstName, row, column, confirmationNumber)

            err = "Congratulations, " + firstName + "! You will be assigned to Row " + row + ", Seat " + column + " for your upcoming trip. We hope you enjoy your trip! \n Your e-ticket number is: " + confirmationNumber
            chart = presentChart(initialChart)
            return render_template("reservations.html", title="Reservations", err=err, chart=chart, form=form,  template="form-template")

        else:
            err = "ERROR! Row " + row + ", Seat " + column + " is already taken. Please make a different selection."



    chart = presentChart(initialChart)

    return render_template("reservations.html", title="Reservations", err=err, chart=chart, form=form, template="form-template")
