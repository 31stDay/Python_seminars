"""
Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

"""
import csv

def print_file():
    with open('phone_book.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)


def write_file():
    with open('phone_book.csv', 'a+', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        print('Введите следующие данные: ')
        surname = input('Фамилия: ')
        name = input('Имя: ')
        p_surname = input('Отчество: ')
        phone = input('Телефон: ')
        new_entry = surname + ';' + name + ';' + p_surname + ';' + phone
        csv_file.write(new_entry)
        csv_file.write("\n")
        print('Новая запись создана.')


def search_for_entry():
    search_word = input('Введите фамилию, имя, отчество или телефон: ')
    with open('phone_book.csv', 'w', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            for field in row:
                if(search_word == field):
                    print(row)
            else:
                print('Строки, удовлетворяющие условиям поиска, не найдены')


def main():
    flag = True
    while flag:
        n = int(input(
            '1 - вывод из справочника, 2 - запись в справочник, 3 - поиск, 0 - выход\n'))
        if n == 1:
            print_file()
        elif n == 2:
            write_file()
        elif n == 3:
            search_for_entry()
        elif n == 0:
            flag = False
        else:
            print('Введено некорректное значение')


if __name__ == '__main__':
    main()


# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
