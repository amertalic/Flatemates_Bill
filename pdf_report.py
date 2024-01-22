import os.path
import webbrowser

from fpdf import FPDF

from bill import Bill
from flatmate import Flatmate


class PdfReport:
    """
    Creates a PDF report file that contains data about the flatmates and their payment amounts.
    """

    def __init__(self, filename: str):
        self.filename = filename

    def generate(self, flatmate1: Flatmate, flatmate2: Flatmate, bill: Bill) -> None:
        """
        Generates a PDF file that includes the logo, names, and amounts each flatmate needs to pay.
        Opens the output PDF file in the default web browser after finishing.
        """
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add icon
        pdf.image("storage/416404_bill_receipt_icon.png", w=30, h=30)
        pdf.ln(10)

        # Insert title.
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=0, align="C", ln=1)

        # Insert Period label and value.
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert Flatmate names and pay values.
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        file_path = f"outputfiles/{self.filename}"
        pdf.output(file_path)

        # Open file in browser depending on your operating system.
        if os.name == "nt":
            webbrowser.open(file_path)
        else:
            webbrowser.open(f"file://{os.path.realpath(file_path)}")
