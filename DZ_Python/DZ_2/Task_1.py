# Задача №1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
#   0,56 -> 11
number = str(input("Введите вещественное число = "))
sum = 0
for i in range(0, len(number)):
    if number[i] != '.':
        sum += int(number[i])
print(sum)

# Второй вариант с сортировкой символа точки.
# number = str(input("Введите вещественное число = "))
# sum = 0
# for i in range(len(number)):
#     if number[i].isdigit():
#         sum += int(number[i])
# print(sum)