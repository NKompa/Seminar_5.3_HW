# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> 12

import random

list_len = int(input('Введите длину списка: '))
num_list = []
for i in range(list_len):
    num_list.append(random.randint(0,21))
print(num_list)

sum = 0
for i in range(len(num_list)):
    if i %2 ==1:
        sum += num_list[i]
print(sum)