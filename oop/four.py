class Phone:
    def __init__(self, make: str, price: int, years_used: int) -> None:
        self.make = make
        self.price = price
        self.years_used = years_used

    def calc_depreciated(self) -> float:
        value = self.price

        for i in range(self.years_used):
            value += -(value * 0.67)

        return round((self.price - value), 2)

    def __str__(self) -> str:
        return f"Phone info: make {self.make}, price {self.price}, price after depreciatied: {self.calc_depreciated()}"


makes = ["Samsung", "Apple", "Blackberry"]
model_prices = [1900, 2300, 1000]
years_useds = [2, 3, 4]


def recur(n: int) -> int:
    if n == 3:
        return

    print(Phone(makes[n], model_prices[n], years_useds[n]))

    recur(n + 1)

recur(0)
