class Bill:
    """
    Object that contains data about a bill, like total amount and period.
    """

    def __init__(self, amount: [int, float], period: str):
        self.amount = amount
        self.period = period
