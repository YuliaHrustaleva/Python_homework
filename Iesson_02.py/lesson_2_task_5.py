#Напишите функцию month_to_season(), 
# которая принимает один аргумент — номер месяца — и возвращает название сезона, 
# к которому относится этот месяц. Например, передаем 2, на выходе получаем «Зима».


def month_to_season(month: int) -> str:
    
   
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        raise ValueError("Номер месяца должен быть от 1 до 12")


if __name__ == "__main__":
    print(month_to_season(2))   # Зима
    print(month_to_season(6))   # Лето
    print(month_to_season(10))  # Осень