from bill import Bill
from flatmate import Flatmate
from pdf_report import PdfReport

bill_amount = int(input("Hey user, enter the bill amount? "))
bill_period = input("Please enter the period for the provided bill (ie. 'Month YYYY')? ")
the_bill = Bill(bill_amount, bill_period)

flatmate_1_name = input("Pleas enter the name of flatmate 1? ")
flatmate_1_days = int(input(f"Please enter how manny days did {flatmate_1_name} stay in house during bill period? "))
flatmate_1 = Flatmate(flatmate_1_name, flatmate_1_days)

flatmate_2_name = input("Pleas enter the name of flatmate 2? ")
flatmate_2_days = int(input(f"Please enter how manny days did {flatmate_2_name} stay in house during bill period? "))
flatmate_2 = Flatmate(flatmate_2_name, flatmate_2_days)

flatmate_1.pays(the_bill, flatmate_2)
flatmate_2.pays(the_bill, flatmate_1)

filename = f"report_{bill_period.replace(' ', '_').lower()}.pdf"

report = PdfReport(filename)
report.generate(flatmate_1, flatmate_2, the_bill)
