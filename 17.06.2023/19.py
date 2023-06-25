my_list = [1, 2, 3, 4, 5]
k = int(input('Введите число'))
my_list_2 = my_list[k:] + my_list[:k]
print(my_list, my_list_2)