# Ввести месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Два решения через list и dict

my_list_season = [['Зима', 1, 2, 12], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]
my_dict_season = {'Зима': (1, 2, 12), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}

# Проверка корректности ввода номера месяца
while True:
    try:
        month_season = int(input('Введите номер месяца года(1-12): '))
        if month_season < 1 or month_season > 12:
            print("\x1b[31m", 'Ошибка! Номер месяца только в интервале 1-12: ', "\x1b[0m")
            continue
        break
    except ValueError:
        print("\x1b[31m", 'Ошибка! Вводите только целые числа!', "\x1b[0m")

# Решение через dict
for i in my_dict_season.keys():
    if month_season in my_dict_season[i]:
        print("\nРешение через dict: ", "\x1b[34m", i, "\x1b[0m")

# Решение через list
for i in my_list_season:
    list_season = i
    for n in list_season:
        if month_season == n:
            print("Решение через list: ", "\x1b[34m", list_season[0], "\x1b[0m")
