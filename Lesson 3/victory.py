import random

# Список известных людей и их даты рождения
celebrities = {
    "А.С. Пушкин": "06.06.1799",
    "Л.Н. Толстой": "09.09.1828",
    "И.С. Тургенев": "09.11.1818",
    "М.Ю. Лермонтов": "15.10.1814",
    "Ф.М. Достоевский": "11.11.1821",
    "А.П. Чехов": "29.01.1860",
    "Н.В. Гоголь": "01.04.1809",
    "В.М. Гаршин": "14.02.1855",
    "И.А. Бунин": "22.10.1870",
    "А.А. Блок": "28.11.1880",
}


# Функция для преобразования даты в текст
def date_to_text(date_str):
    months = {
        "01": "января",
        "02": "февраля",
        "03": "марта",
        "04": "апреля",
        "05": "мая",
        "06": "июня",
        "07": "июля",
        "08": "августа",
        "09": "сентября",
        "10": "октября",
        "11": "ноября",
        "12": "декабря",
    }
    day, month, year = date_str.split(".")
    return f"{int(day)} {months[month]} {year} года"


# Викторина
while True:
    selected_celebrities = random.sample(list(celebrities.items()), 5)
    correct_count = 0

    for name, birth_date in selected_celebrities:
        user_input = input(f"Введите дату рождения {name} в формате 'dd.mm.yyyy': ")
        if user_input == birth_date:
            correct_count += 1
        else:
            print(f"Неправильно! Правильный ответ: {date_to_text(birth_date)}")

    total_questions = len(selected_celebrities)
    incorrect_count = total_questions - correct_count
    correct_percentage = (correct_count / total_questions) * 100

    print(f"Количество правильных ответов: {correct_count}")
    print(f"Количество неправильных ответов: {incorrect_count}")
    print(f"Процент правильных ответов: {correct_percentage:.2f}%")

    restart = input("Хотите начать заново? (да/нет): ").strip().lower()
    if restart != "да":
        break
