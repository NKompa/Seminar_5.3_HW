# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
list = [round(random.uniform(1, 10), 2) for x in range(5)]
print(list)

list2 = [round((i%1),2) for i in list]
min = 1
max = 0
for i in list2:
    if i < min and i!=0: min = i        # дробная часть 0 будет минимальным значением. Условие задачи немного запутывает.
    if i > max: max = i
print(round((max-min),2))