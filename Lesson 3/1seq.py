# Пользователь вводит количество элементов будущего списка
n = int(input("Введите количество элементов: "))
lst = []

# Ввод элементов списка
for i in range(n):
    element = int(input(f"Введите {i+1} элемент: "))
    lst.append(element)

# Сортировка списка и вывод на экран
lst.sort()
print("Отсортированный список:", lst)
