# Задача № 1.  Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, 
#              которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# import random


# def fillList(n):  # заполнение списка
#     filled_list = []
#     for i in range(0, n-1):
#         filled_list.append(random.randint(-10, 11))
#     print(filled_list)
#     return filled_list


# def sumList(x):  # расчет суммы элементов на нечетных поз-х
#     sum = 0
#     for i in range(0, len(x)):
#         if i % 2 != 0:
#             sum += x[i]
#     return sum


# n = int(input("enter length list of numbers N = "))
# some_list = []
# some_list = fillList(n)
# sum_of_numbers = sumList(some_list)
# print("сумма чисел на нечетных позициях = ", sum_of_numbers)


import random
n = int(input("enter length list of numbers N = "))

def fillList(n):  # заполнение списка
    filled_list = [random.randint(-10, 11) for _ in range(-10,10)]
    print(filled_list)
    return filled_list

numbers_list = fillList(n)
sum_odd = sum(numbers_list[item] for item in range(1, len(numbers_list), 2))
odd_el = str([numbers_list[item] for item in range(1, len(numbers_list), 2)]).strip('[]')
print(f'Для списка {numbers_list} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')