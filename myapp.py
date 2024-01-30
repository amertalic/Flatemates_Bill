from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

from flatemates_bill.bill import Bill
from flatemates_bill.flatmate import Flatmate

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html", billform=bill_form)


class ResultPage(MethodView):

    def post(self):
        billform = BillForm(request.form)

        the_bill = Bill(float(billform.amount.data), billform.period.data)

        flatmate_1 = Flatmate(billform.name1.data, int(billform.days1.data))
        flatmate_2 = Flatmate(billform.name2.data, int(billform.days2.data))

        flatmate_1.pays(the_bill, flatmate_2)
        flatmate_2.pays(the_bill, flatmate_1)

        flatmate2_pay = str(round(flatmate_2.pays(the_bill, flatmate_1), 2))
        flatmate1_pay = str(round(flatmate_1.pays(the_bill, flatmate_2), 2))

        return render_template("results_page.html",
                               period=the_bill.period,
                               name1=flatmate_1.name,
                               amount1=flatmate1_pay,
                               name2=flatmate_2.name,
                               amount2=flatmate2_pay,
                               )


class BillForm(Form):
    amount = StringField("Bill Amount: ", default=100)
    period = StringField("Bill Period: ", default="January 2024")

    name1 = StringField("Name: ", default="Omar")
    days1 = StringField("Days in the house: ", default=30)

    name2 = StringField("Name: ", default="Daniel")
    days2 = StringField("Days in the house: ", default=30)

    button = SubmitField("Calculate")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/billform", view_func=BillFormPage.as_view("bill_form_page"))
app.add_url_rule("/results", view_func=ResultPage.as_view("results_page"))

app.run(debug=True)
