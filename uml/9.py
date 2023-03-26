class School:
    def __init__(self):
        self.set_data()
        print(self.print_data())

    def set_data(self) -> None:
        """
            Sets the data for the class

            name: str, num_of_students: int, num_of_classrooms: int
        """
        self.name = input("Name of School: ")
        self.num_of_students = int(input("Number of students: "))
        self.num_of_classrooms = int(input("Number of classrooms: "))


    def average(self) -> int:
        return int(round((self.num_of_students / self.num_of_classrooms), 0))

    def print_data(self) -> str:
        return f"\nSchool name: {self.name}\nNumber of students: {self.num_of_students}\nNumber of classrooms: {self.num_of_classrooms}\nAverage students per class: {self.average()}"

if __name__ == "__main__":
    School()
