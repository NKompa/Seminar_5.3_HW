# Напишите программу, которая будет преобразовывать десятичное число в двоичное. 45 -> 101101, 3 -> 11, 2 -> 10

decimal = int(input('Введите число: '))
binary = []
while True:
    remainder = decimal%2
    binary.append(remainder)
    decimal //=2
    if decimal == 0 or decimal == 1:
        binary.append(decimal)
        break
binary = reversed(binary)
print(''.join(map(str,binary)))