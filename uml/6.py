class OneString:
    def __init__(self, one_string: str):
        self.one_string = one_string

    def __str__(self):
        """
        Return the string
        """
        return f"This string stores: '{self.one_string}'"


if __name__ == "__main__":
    print(OneString("Sussy among us"))
