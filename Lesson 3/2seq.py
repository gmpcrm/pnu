# Пользователь вводит любые цифры через запятую
input_str = input("Введите элементы списка через запятую: ")

# Определение разделителя
if "," in input_str:
    delimiter = ","
elif ";" in input_str:
    delimiter = ";"
elif "/" in input_str:
    delimiter = "/"
else:
    delimiter = ","

# Создание списка и фильтрация уникальных элементов
lst = input_str.split(delimiter)
unique_lst = [int(x) for x in lst if lst.count(x) == 1]

# Вывод уникальных элементов
print("Результат:", unique_lst)
