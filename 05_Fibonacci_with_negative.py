# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Введите число больше 1: '))
list1 = [0,1]
list2 = [0,1]
for i in range(0,number-1):
    list1.append(list1[i]+list1[i+1])
    list2.append(list2[i]-list2[i+1])
list1.remove(0)
list2.reverse()
Fibonacci = list2 + list1
print(Fibonacci)
