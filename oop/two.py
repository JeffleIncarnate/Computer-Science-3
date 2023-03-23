class Movie:
    def __init__(
        self,
        title: str,
        producer: str,
        director: str,
        date: str,
        length: int,
        rating: int,
        genere: str,
        cost: int,
        revenue: int,
    ) -> None:
        self.title = title
        self.producer = producer
        self.director = director
        self.date = date
        self.length = length
        self.rating = rating
        self.genere = genere
        self.cost = cost
        self.revenue = revenue

    def calculate(self) -> float:
        return round((self.revenue - self.cost), 2)

    def __str__(self) -> str:
        profit = "profit"
        if str(self.calculate())[0] == "-":
            profit = "loss"

        return (
            f'The movie "{self.title}" made a {profit} of {str(abs(self.calculate()))}'
        )


print(
    Movie(
        "[INSERT NAME]",
        "Dhruv Rayat",
        "Dhruv Rayat",
        "01/01/2025",
        "2 hours",
        5,
        "Thriller",
        1_000_000,
        500_000,
    )
)
