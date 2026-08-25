#Создайте функцию is_year_leap, принимающую 1 аргумент — год (число) — и возвращающую True, 
# если год високосный, и False  — если иначе


def is_year_leap(year: int) -> bool:
                        
    return year % 4 == 0      #Возвращает True, если год високосный, иначе False.

test_year = 2024  # Выбираем год для проверки

result = is_year_leap(test_year)  # Вызываем функцию и сохраняем результат в переменную

print(f"год {test_year}: {result}")  # Выводим результат в консоль