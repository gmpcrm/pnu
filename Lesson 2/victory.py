# Викторина по годам рождения известных людей
questions = {
    "Пушкин": 1799,
    "Толстой": 1828,
    "Тургенев": 1818,
    "Лермонтов": 1814,
    "Достоевский": 1821,
}

while True:
    correct = 0
    for person, year in questions.items():
        user_input = int(input(f"Введите год рождения {person}: "))
        if user_input == year:
            correct += 1

    total = len(questions)
    wrong = total - correct
    correct_percent = (correct / total) * 100
    wrong_percent = 100 - correct_percent

    print(f"Правильных ответов: {correct}")
    print(f"Ошибок: {wrong}")
    print(f"Процент правильных ответов: {correct_percent:.2f}%")
    print(f"Процент ошибок: {wrong_percent:.2f}%")

    restart = input("Хотите начать заново? (да/нет): ").strip().lower()
    if restart != "да":
        break
