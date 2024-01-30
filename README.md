# Shared Bill Splitter

This Python script helps you split bills between two flatmates and generates a PDF report detailing their contributions.
The script uses the Bill, Flatmate, and PdfReport classes.
The only external requirement is the fpdf library, which you can install by see `requirements.txt` bellow:

## Usage

### Command Line Interface (CLI) App

Run the CLI script by executing the following command in your terminal:

```bash
python cli_main.py
```

1. You will be prompted to enter the following information:

   - **Bill Amount:** Enter the total amount of the bill.
   - **Bill Period:** Enter the period for the provided bill (e.g., 'Month YYYY').
   - **Flatmate 1:**
       - Enter the name of Flatmate 1.
       - Enter the number of days Flatmate 1 stayed in the house during the bill period.
   - **Flatmate 2:**
       - Enter the name of Flatmate 2.
       - Enter the number of days Flatmate 2 stayed in the house during the bill period.

2. The script will calculate the share of each flatmate and generate a PDF report named `report_month_year.pdf`.

### Flask HTML Web App

To run the web app, execute the following command:

```bash
python myapp.py
```

Visit [http://localhost:5000/](http://localhost:5000/) in your web browser to access the web interface.

## Requirements

Make sure you have the fpdf library installed. You can install it using:

```bash
pip install fpdf
```

Additionally, for the Flask web app, you may need to install Flask:

```bash
pip install flask
```

# Design

## Description

The application streamlines the process of splitting bills between two flatmates. It accepts the total amount of a bill for a specific period, along with the number of days each flatmate stayed in the house during that period. The app then calculates and displays the contribution each flatmate needs to make towards the bill. The app also generates a detailed PDF report containing the flatmates' names, billing period, and individual payment amounts.

## Objects

1. **Bill:**
   - `amount`: Total amount of the bill.
   - `period`: Period for which the bill is issued.
2. **Flatmate:**
   - `name`: Name of the flatmate.
   - `days_in_house`: Number of days the flatmate stayed in the house during the bill period.
   - `pays(bill)`: Method to calculate the contribution of the flatmate towards the bill.
3. **PdfReport:**
   - `filename`: Name of the PDF file to be generated.
   - `generate(flatmate1, flatmate2, bill)`: Method to create a PDF report with information about the flatmates, the billing period, and their respective contributions.

Additionally, the web app runs using `myapp.py`, while the CLI app runs using `cli_main.py`.