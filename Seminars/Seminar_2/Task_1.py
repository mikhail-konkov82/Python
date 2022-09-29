# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример: Для N = 5: 1, -3, 9, -27, 81

Number = int(input('Введите число N: '))

result = []
for degree in range(Number):
    result.append(str((-3)**degree))

print(", ".join(result), end=".")
