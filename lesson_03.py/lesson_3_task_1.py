# импортировали из файла user.py класс User 
from user import User

# создаем экземпляр класса User И сохраняем в переменную
my_user = User("Алена", "Фролова")

# вызываем все методы

my_user.print_first_name()
my_user.print_last_name()
my_user.print_full_name()


