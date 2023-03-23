class BasketballPlayer:
    def __init__(
        self,
        name: str,
        player_num: int,
        num_of_games_played: int,
        total_goals_scored: int,
    ) -> None:
        self.name = name
        self.player_num = player_num
        self.num_of_games_played = num_of_games_played
        self.total_goals_scored = total_goals_scored

    def calculate(self) -> float:
        return round((self.total_goals_scored / self.num_of_games_played), 2)

    def __str__(self) -> str:
        return f"The player {self.name} has an average score over his entire carrer of {self.calculate() * 100}%"


print(BasketballPlayer("Dhruv", 58, 10, 5))
