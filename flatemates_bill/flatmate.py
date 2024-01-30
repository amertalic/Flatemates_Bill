from flatemates_bill.bill import Bill


class Flatmate:
    """
    Object of a person having attributes that contain information such as name,
    how manny days it stayed in the house and calculates how much the object needs to pay.
    """

    def __init__(self, name: str, days_in_house: int):
        self.pay = None
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill: Bill, flatmate_other: 'Flatmate') -> [float, int]:
        weigth = self.days_in_house / (self.days_in_house + flatmate_other.days_in_house)

        self.pay = bill.amount * weigth

        print(f"{self.name} stayed for {self.days_in_house} and needs to pay {self.pay} for {bill.period}.")
        return self.pay
