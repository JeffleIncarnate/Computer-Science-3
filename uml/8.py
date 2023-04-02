class TeamSport:
    def __init__(self, sport: str, num_of_playes: int):
        self.store_info(sport, num_of_playes)

    def store_info(self, sport: str, num_of_playes: int) -> None:
        self.sport = sport
        self.num_of_playes = num_of_playes

    def __str__(self):
        return f"{self.sport.title()} is the team sport\nThere are {self.num_of_playes} in a {self.sport.title()} team\n"

if __name__ == "__main__":
    print(TeamSport("Cricket", 11))
    print(TeamSport("Netball", 7))