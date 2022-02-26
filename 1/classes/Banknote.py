class Banknote:
    def __init__(self, currency: str, nominal_value: int) -> None:
        self.currency = currency
        self.nominal_value = nominal_value

    def __str__(self):
        return f"{self.nominal_value} {self.currency}"
