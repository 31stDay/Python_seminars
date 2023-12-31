from tabulate import tabulate
import csv


def readfile(filename):
    read_data = [i.strip().split(';') for i in open(filename, 'r', encoding='utf-8')]
    # read_data = []
    # with open('tel.txt', 'r', encoding='utf-8') as file:
    #     for elem in file:
    #         read_data.append(elem.split())
    return read_data


def menu():
    print('===============================')
    print('Выберите одно из действий:')
    print('1 - вывести справочник на экран')
    print('2 - произвести экпорт данных')
    print('3 - поиск абонентов')
    print('4 - удаление из справочника по id')
    print('5 - добавление записи в справочник')
    print('0 - выход из программы')

 
def printinfo(data):
    # print('id \t Фамилия Имя Отчество \t номер телефона')
    # for elem in data:
    #     print(*elem, sep='\t')
    print(tabulate(data, headers=['id', 'ФИО', 'Телефон'], tablefmt='orgtbl'))

def export_to_csv(data):
    with open('example2.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print('Экспорт завершён')


def search(data):
    what = input('Что ищем? ')
    searched_data = []
    for string in data:
        for elem in string:
            if (what in elem) and string not in searched_data:
                searched_data.append(string)
    if searched_data:
        printinfo(searched_data)
    else:
        print('Строки, удовлетворяющие условиям поиска, не найдены')


def delete(data):
    id = input('Введите id для удаления: ')
    new_data = []
    for elem in data:
        if elem[0] != id:
            new_data.append(elem)
    return new_data


def add_record(data):
    id = input('Введите id нового человека: ')
    name = input('Введите ФИО нового человека: ')
    tel = input('Введите номер телефона: ')
    data.append((id, name, tel))
    return data

def save(data):
    with open('tel.txt', 'w', encoding='utf-8') as file:
        for elem in data:
            stroka = ';'.join(elem) + '\n'
            file.write(stroka)


def main():
    my_choice = -1
    changed = False
    # словарь номеров команд и привязанных к ним функций
    operations = {
        1: printinfo,
        2: export_to_csv,
        3: search,
        4: delete,
        5: add_record
        }
    data = readfile('tel.txt')
    while my_choice != 0:
        menu()
        my_choice = int(input('Введите команду: '))
        if 1 <= my_choice <= 3:
            operations[my_choice](data)
        elif 4 <= my_choice <= 5:
            changed = True
            data = operations[my_choice](data)
        elif my_choice == 0:
            if changed:
                print('Данные были изменены. Идёт сохранение данных')
                save(data)
            print('До свидания')
        else:
            print('Введена неправильная команда')


if __name__ == '__main__':
    main()