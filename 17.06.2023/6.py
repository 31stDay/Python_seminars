"""
Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no
"""
first_triple = 0
second_triple = 0
ticket_number = int(input('Enter 6 digit ticket number: '))
t_ticket_number = ticket_number
if (ticket_number > 99000) and (ticket_number < 1000000):
    while (t_ticket_number > 0):
        while (t_ticket_number > 999):
            second_triple = second_triple + t_ticket_number % 10
            t_ticket_number = t_ticket_number // 10
        first_triple = first_triple + t_ticket_number % 10
        t_ticket_number = t_ticket_number // 10
    if (first_triple == second_triple):
        print('Yes')
    else:
        print('No')
else:
    print('You\'ve enter the wrong number!')


