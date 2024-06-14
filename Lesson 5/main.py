import importlib.util
import os
from pathlib import Path
import shutil
import platform


# так как уже было сделано имя папки с пробелом, чтобы ничего
# не сломалось, импортируем модуль с помощью функции
# иначем можно было бы просто сделать
# import use_functions from lesson4.use_functions
def import_module_from_path(module_name, module_path):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Импортируем use_functions
use_functions = import_module_from_path(
    "use_functions",
    str(Path(__file__).resolve().parents[1] / "Lesson 4" / "use_functions.py"),
)

victory = import_module_from_path(
    "victory", str(Path(__file__).resolve().parents[1] / "Lesson 3" / "victory.py")
)


def main_menu():
    print("\nВыберите действие:")
    print("1. Создать папку")
    print("2. Удалить (файл/папку)")
    print("3. Копировать (файл/папку)")
    print("4. Просмотр содержимого рабочей директории")
    print("5. Посмотреть только папки")
    print("6. Посмотреть только файлы")
    print("7. Просмотр информации об операционной системе")
    print("8. Создатель программы")
    print("9. Играть в викторину")
    print("10. Мой банковский счет")
    print("11. Смена рабочей директории")
    print("12. Выход")


def create_folder():
    folder_name = input("Введите название папки: ")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Папка '{folder_name}' успешно создана.")
    else:
        print("Такая папка уже существует.")


def delete_file_or_folder():
    name = input("Введите название файла или папки для удаления: ")
    if os.path.isfile(name):
        os.remove(name)
        print(f"Файл '{name}' успешно удален.")
    elif os.path.isdir(name):
        shutil.rmtree(name)
        print(f"Папка '{name}' успешно удалена.")
    else:
        print("Файл или папка не найдены.")


def copy_file_or_folder():
    src = input("Введите название файла или папки для копирования: ")
    dest = input("Введите новое название файла или папки: ")
    if os.path.exists(src):
        if os.path.isfile(src):
            shutil.copy(src, dest)
            print(f"Файл '{src}' успешно скопирован в '{dest}'.")
        elif os.path.isdir(src):
            shutil.copytree(src, dest)
            print(f"Папка '{src}' успешно скопирована в '{dest}'.")
    else:
        print("Файл или папка не найдены.")


def view_directory_contents():
    items = os.listdir()
    for item in items:
        print(item)


def view_only_folders():
    items = os.listdir()
    folders = [item for item in items if os.path.isdir(item)]
    for folder in folders:
        print(folder)


def view_only_files():
    items = os.listdir()
    files = [item for item in items if os.path.isfile(item)]
    for file in files:
        print(file)


def view_os_info():
    print("Информация об операционной системе:")
    print(platform.system(), platform.release())


def creator_info():
    print("Создатель программы: Джон Смитт")


def play_quiz():
    print("Запуск викторины...")
    victory.main()


def bank_account():
    print("Запуск программы 'Мой банковский счет'...")
    use_functions.main()


def change_working_directory():
    new_directory = input(
        "Введите полный или относительный путь к новой рабочей директории: "
    )
    if os.path.isdir(new_directory):
        os.chdir(new_directory)
        print(f"Рабочая директория изменена на {new_directory}")
    else:
        print("Указанная директория не существует.")


def main():
    while True:
        main_menu()
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            create_folder()
        elif choice == "2":
            delete_file_or_folder()
        elif choice == "3":
            copy_file_or_folder()
        elif choice == "4":
            view_directory_contents()
        elif choice == "5":
            view_only_folders()
        elif choice == "6":
            view_only_files()
        elif choice == "7":
            view_os_info()
        elif choice == "8":
            creator_info()
        elif choice == "9":
            play_quiz()
        elif choice == "10":
            bank_account()
        elif choice == "11":
            change_working_directory()
        elif choice == "12":
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()
