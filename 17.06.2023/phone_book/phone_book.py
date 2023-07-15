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
# if __name__ == "__main__":
#     menu()  

def menu():
    flag = True
    while flag:
        n = int(input('1 - вывод из справочника, 2 - запись в справочник, 3 - поиск, 0 - выход\n'))
        if n == 1:
            read_file()
        elif n == 2:
            write_file()
        elif n == 3:
            search_for_entry() 
        elif n == 0:
            flag = False   
        else:
            print('Введите корректное значение')

def read_file():
    with open('phone_book.csv', 'r', encoding = 'utf-8') as f:
        for string in f:
            print(*string.strip().split(";"))

def write_file():
    with open('phone_book.csv', 'a', encoding = 'utf-8') as f:
        print('Введите следующие данные: ')
        surname = input('Фамилия: ')
        name = input('Имя: ')
        p_surname = input('Отчество: ')
        phone = input('Телефон: ')

        new_entry = surname + ';' + name + ';' + p_surname + ';' + phone
        f.writelines(new_entry)
        print('Новая запись создана.')

def search_for_entry():
    with open('phone_book.csv', 'r', encoding= 'utf-8') as f:
        search_word = input('Введите фамилию, имя, отчество или телефон: ')
        for string in f:
            for word in string:
                if (word == search_word):
                    print(*string.strip().split(";"))


 
menu()    


# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.






