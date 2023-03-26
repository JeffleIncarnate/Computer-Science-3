from datetime import datetime

class Person:
    def __init__(self, name: str, birth_year: int, is_male: bool):
        self.name = name
        self.birth_year = birth_year
        self.is_male = is_male
        self.current_year = datetime.now().year

    def get_age(self):
        """
            Returns the aproximate age of the user.
        """
        return self.current_year - self.birth_year

    def __str__(self):
        """
            Returns all the info for a user
        """
        return f"User name: {self.name.title()}\nAge: {self.get_age()}\nGender: {'male' if self.is_male else 'female'}\n"

if __name__ == "__main__":
    print(Person("dhruv", 2006, True))
    print(Person("snoopy", 2015, True))