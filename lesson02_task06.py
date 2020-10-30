# Структура данных «Товары», это список кортежей, # Каждый кортеж хранит инфо об отдельном товаре
# В кортеже два элемента — номер товара и словарь с характеристиками и их параметрами:
# (характеристики: название, цена, количество, единица измерения)
# Данные(значения параметров) вводят пользователи
# Далее  - необходимо собрать аналитику о товарах, реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров

# функция проверки на ввод чисел(+целые +дробные +отрицательные)
def chek_num(user_string):
    while True:
        try:
            param_num = int(input(user_string))
            return param_num
        except ValueError:
            print("\x1b[31m", 'Ошибка! Вводите только числа!', "\x1b[0m")


product_list = []
analyst_dict = {}
product_dict = {}
product_list_temp = []
product_tuple = ()
count = 0

# создаем структуру Товары, данные вводит пользователь
# это будет список из кортежей, кортежи состоят из номера товара и словарей с параметрами

while True:
    product_name = input('Введите название\x1b[34m(завершить ввод - "q" или "й"):\x1b[0m ')
    if product_name == "q" or product_name == "й":
        break
    product_price = chek_num('Введите стоимость: ')
    product_number = chek_num('Введите количество: ')
    product_unit = input("Введите единицу измерения: ")
    product_dict["название"] = product_name
    product_dict["цена"] = product_price
    product_dict["количество"] = product_number
    product_dict["ед"] = product_unit
    count += 1
    product_list_temp.append(count)
    product_list_temp.append(product_dict)
    product_tuple = tuple(product_list_temp)
    product_list.append(product_tuple)
    product_dict = {}
    product_list_temp = []

print('\n\x1b[34mСоздан список - структура Товаров\x1b[0m\n', product_list)
print(f'\n\x1b[34mВывод на экран структуры Товары и их параметров(кортежи из списка):\x1b[0m')
for count in product_list:
    print(count)

# строим аналитику о товарах в виде словаря на введенных товарах и их параметрах,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров

product_list_name = []
product_list_cost = []
product_list_num = []
product_list_unit = []

for i in range(len(product_list)):
    product_list_temp = list(product_list[i])
    product_dict2 = product_list_temp[1]
    product_list_name.append(product_dict2.setdefault('название'))
    product_dict["название"] = product_list_name
    product_list_cost.append(product_dict2.setdefault('цена'))
    product_dict["цена"] = product_list_cost
    product_list_num.append(product_dict2.setdefault('количество'))
    product_dict["количество"] = product_list_num
    product_list_unit.append(product_dict2.setdefault('ед'))
    product_dict["ед"] = product_list_unit

print(f'\n\x1b[34mВывод на экран аналитики:\x1b[0m ')
for count in product_dict:
    print(f'{count:>10}  >>>  {product_dict[count]}')
