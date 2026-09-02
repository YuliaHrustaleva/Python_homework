class User:

# конструктор класса
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

# метод для печати только имени
    def print_first_name(self):
        print(self.first_name)

# метод для печати только фамилии
    def print_last_name(self):
        print(self.last_name)

# метод для печати имени и фамилии
    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")         

         


