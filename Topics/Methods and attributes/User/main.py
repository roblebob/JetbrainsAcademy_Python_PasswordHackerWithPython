class User:
    def __init__(self, _name, _surname, _age, _country):
        self.name = _name
        self.surname = _surname
        self.age = _age
        self.country = _country


    def user_information(self):
        print(f"{self.name} {self.surname} is {self.age} years old and lives in {self.country}.")


name = input()
surname = input()
age = int(input())
country = input()

user = User(name, surname, age, country)
user.user_information()
