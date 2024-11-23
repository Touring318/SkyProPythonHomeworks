# Високосный год
# Присваиваем переменной любое значение, так как фунция в любом
# случае присвоит ей значение по результатам своей работы


def is_year_leap(year):
    if (year % 4) == 0:
        year_leap = True
    else:
        year_leap = False
    return year_leap


year = int(input("Введите четырехзначный год: "))
print("год " + str(year) + ": " + str(is_year_leap(year)))
