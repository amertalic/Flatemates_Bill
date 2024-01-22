# Shared Bill Splitter
This Python script helps you split bills between two flatmates and generates a PDF report detailing their contributions.
The script uses the Bill, Flatmate, and PdfReport classes.
The only external requirement is the fpdf library, which you can install by see Requirements bellow:

## Usage
Run the script by executing the following command in your terminal:
```bash
python main.py
```

1. You will be prompted to enter the following information:
- Bill Amount: Enter the total amount of the bill.
- Bill Period: Enter the period for the provided bill (e.g., 'Month YYYY').
- Flatmate 1: 
  - Enter the name of Flatmate 1.
  - Enter the number of days Flatmate 1 stayed in the house during the bill period.
- Flatmate 2:
  - Enter the name of Flatmate 2. 
  - Enter the number of days Flatmate 2 stayed in the house during the bill period.
2. The script will calculate the share of each flatmate and generate a PDF report named report_month_year.pdf.

## Requirements
Make sure you have the fpdf library installed. You can install it using:
```bash
pip install fpdf
```


# Design

## Description
It is a Python app designed to streamline the process of splitting bills between two flatmates. The application takes as input the total amount of a bill for a specific period, along with the number of days each flatmate stayed in the house during that period. It then calculates and displays how much each flatmate needs to contribute towards the bill. Additionally, the app generates a detailed PDF report containing the names of the flatmates, the billing period, and the individual payment amounts.

## Objects
1. Bill:
   2. amount: Total amount of the bill.
   3. period: Period for which the bill is issued.
2. Flatmate:
   3. name: Name of the flatmate.
   4. days_in_house: Number of days the flatmate stayed in the house during the bill period. 
   5. pays(bill): Method to calculate the contribution of the flatmate towards the bill.
3. PdfReport:
   4. filename: Name of the PDF file to be generated.
   5. generate(flatmate1, flatmate2, bill): Method to create a PDF report with information about the flatmates, the billing period, and their respective contributions.