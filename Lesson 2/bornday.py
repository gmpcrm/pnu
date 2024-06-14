# Спрашиваем год и день рождения А.С. Пушкина
pushkin_birth_year = 1799
pushkin_birth_day = 6

year_input = int(input("Введите год рождения А.С. Пушкина: "))

if year_input == pushkin_birth_year:
    day_input = int(input("Введите день рождения А.С. Пушкина: "))
    if day_input == pushkin_birth_day:
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год рождения")
