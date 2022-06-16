import mysql.connector
from flask import Flask, request, render_template

from sql_func import *

app = Flask(__name__, template_folder="template")

@app.route('/', methods=["GET", "POST"])
def table():
    income_res = get_values('income')
    expense_res = get_values('expense')

    inc_tot, exp_tot = 0, 0
    for i in income_res:
        inc_tot += i['income_amount']

    for i in expense_res:
        exp_tot += i['expense_amount']

    return render_template("index.html", total=[inc_tot, exp_tot])

@app.route('/expense', methods=['GET', 'POST'])
def expense():
    # Add new expense if the function is called as POST method
    if request.method == "POST":
        exp_date = request.form.get("date")
        exp_amt = request.form.get("amt")
        exp_desc = request.form.get("desc")
        exp_cat = request.form.get("cat")

        insert(exp_date, exp_amt, exp_desc, exp_cat, 'expense')

    json_data = get_values('expense')
    return render_template("expenses.html", result=json_data)

@app.route('/income', methods=['GET', 'POST'])
def income():
    # Add new income if the function is called as POST method
    if request.method == "POST":
        inc_date = request.form.get("date")
        inc_amt = request.form.get("amt")
        inc_desc = request.form.get("desc")
        inc_cat = request.form.get("cat")

        insert(inc_date, inc_amt, inc_desc, inc_cat, 'income')

    json_data = get_values('income')
    return render_template("income.html", result=json_data)

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    expense_categories = get_categories('expense')
    return render_template("add_expense.html", result=expense_categories)

@app.route('/add_income', methods=['GET', 'POST'])
def add_income():
    income_categories = get_categories('income')
    return render_template("add_income.html", result=income_categories)

if __name__== '__main__':
    # init_db()
    app.run(host='0.0.0.0', debug=True)