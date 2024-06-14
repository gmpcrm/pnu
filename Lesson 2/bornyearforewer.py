# Спрашиваем год рождения А.С. Пушкина до тех пор, пока не введет верный год
pushkin_birth_year = 1799

while True:
    user_input = int(input("Введите год рождения А.С. Пушкина: "))
    if user_input == pushkin_birth_year:
        print("Верно")
        break
    else:
        print("Неверно")
