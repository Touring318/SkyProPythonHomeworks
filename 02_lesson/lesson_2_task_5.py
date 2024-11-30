# Соответствие месяца сезонам года

def month_to_season(month_number):
    if (month_number <= 2) or (month_number == 12):
        print("Зима")
    elif (3 <= month_number <= 5):
        print("Весна")
    elif (6 <= month_number <= 8):
        print("Лето")
    else:
        print("Осень")


month_number = int(input("Введите номер месяца в году: "))
month_to_season(month_number)
