# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

list1_length = int(input('Введите длину списка: '))
list1 = []
for i in range(list1_length):
    list1.append(int(input(f'Введите число {i+1}: ')))
print(list1)

list2 = []
list2_length = -(-len(list1)//2)                # чтобы округлил в бОльшую сторону без функции math

for i in range(list2_length):
    product = list1[i]*list1[len(list1)-1-i]
    list2.append(product)
print(list2)