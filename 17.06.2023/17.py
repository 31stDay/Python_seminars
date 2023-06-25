my_list = [1, 1, 2, 0, -1, 3, 4, 4]
my_list_2 = []

for elem in my_list:
    if elem not in my_list_2:
        my_list_2.append(elem) 
print(len(my_list_2))