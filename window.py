from datetime import date

def input_date():
    print("введите дату: ")
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите день: "))
    return date(year, month, day)

def calculate_days(d):
   return abs((d - date.today()).days)

print("Количество дней: ", calculate_days(input_date()))