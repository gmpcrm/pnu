# Спрашиваем год и день рождения А.С. Пушкина до тех пор, пока не введет верные данные
pushkin_birth_year = 1799
pushkin_birth_day = 6

while True:
    year_input = int(input("Введите год рождения А.С. Пушкина: "))
    if year_input == pushkin_birth_year:
        while True:
            day_input = int(input("Введите день рождения А.С. Пушкина: "))
            if day_input == pushkin_birth_day:
                print("Верно")
                break
            else:
                print("Неверный день рождения")
        break
    else:
        print("Неверный год рождения")
