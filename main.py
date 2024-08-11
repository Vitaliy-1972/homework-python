i = 3
dict_print = dict()
while i != 0:
    a = input('Введите дату: ')
    b = input('Введите задачу: ')
    dict_print[a] = b
    i -= 1
for key, value in dict_print.items():
    print(f'{key} {value}')
