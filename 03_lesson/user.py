# Объявление класса User

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayname(self):
        print(self.first_name)

    def saylastname(self):
        print(self.last_name)

    def sayfullname(self):
        print(f"{self.first_name} {self.last_name}")
