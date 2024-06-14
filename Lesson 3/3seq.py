# Ввод элементов первого списка
first_list_input = input("Введите элементы 1-го списка: ")
first_list = list(map(int, first_list_input.split(",")))

# Ввод элементов второго списка
second_list_input = input("Введите элементы 2-го списка: ")
second_list = list(map(int, second_list_input.split(",")))

# Удаление элементов второго списка из первого списка
result_list = [x for x in first_list if x not in second_list]

# Вывод результата
print("Результат:", result_list)
