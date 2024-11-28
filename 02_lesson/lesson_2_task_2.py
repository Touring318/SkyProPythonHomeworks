# Високосный год

def is_year_leap(year):
    if (year % 4) == 0:
        year_leap = True
    else:
        year_leap = False
    return year_leap


year = int(input("Введите четырехзначный год: "))
print("год " + str(year) + ": " + str(is_year_leap(year)))
