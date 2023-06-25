"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6 
"""
def task11():
    print(
        "Задача №11. Решение в группах Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1."
    )
fibonachi_number = int(input("Введите число из последовательности фибоначи "))
positiv_check = bool(fibonachi_number > 0)
if positiv_check:
        first_number = 1
        second_number = 1
        curent_number = first_number + second_number
        count = 3
        while first_number < fibonachi_number:
            second_number = first_number
            first_number = curent_number
            curent_number = first_number + second_number
            count += 1

        print(
            "Число {} является {} в последовательности фибоначи ".format(
                fibonachi_number, count
            )
        )
        
   





