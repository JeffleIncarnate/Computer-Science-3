class Country:
    def __init__(self, name: str, leader: str, population: int):
        self.name = name
        self.leader = leader
        self.population = population

    def __str__(self) -> str:
        return f"'{self.name}' is a county with the population of {self.population} and it's leader's name is {self.leader}"


countries = ["New Zealand", "Madagascar", "Chad", "Egypt"]
leaders = ["Jacinda", "Dhruv rayat", "Mahanat Beby", "siddy widdy"]
populations = [100000, 20000213, 1207332489, 2194837281]


def recur(i):
    if i == 3:
        return
    print(Country(countries[i], leaders[i], populations[i]))
    recur(i + 1)


recur(0)
