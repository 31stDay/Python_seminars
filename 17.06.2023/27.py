"""
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13
"""
# : a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
string = '''She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells'''
# string = input('Input text: ').lower()

my_list = string.split(' ')
answer = 0
new_list = []
my_dict = {}

for el in my_list:
    if el in my_dict:
        my_dict[el] += 1
    elif el not in my_dict:
        answer += 1
        my_dict[el] = 1
print(my_dict)
print(answer)





"""
atext_user = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".lower().split(" ")

set_1 = set(text_user)
print(len(set_1))

my_dict = {}
for elem in text_user:
    if elem in my_dict:
        my_dict[elem] += 1
    else:
        my_dict[elem] = 1
print(my_dict)

for k,v in my_dict.items():
    if v == max(my_dict.values()):
        print ('{} встречается {} раз '.format(k, v))
"""
