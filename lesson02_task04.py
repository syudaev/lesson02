# Ввести строку из нескольких слов, разделённых пробелами, вывести каждое слово с новой строки
# Строки пронумеровать, если в слово длинное, выводить только первые 10 букв в слове.

my_string = input("Введите строку из нескольких слов: ")
my_list = []

for i in range(my_string.count(' ') + 1):
    my_list = my_string.split()
    print(f'{i + 1} {my_list[i][0:10]}')
