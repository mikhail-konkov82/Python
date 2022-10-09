# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input("Введите число N = "))


def is_simple(num):
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True


def list_of_numbers(n):
    numbers = []
    for i in range(1, n //2 + 1):
        if n % i == 0 and is_simple(i):
            numbers.append(i)
    return numbers       



if __name__ == "__main__":
    print(list_of_numbers(n))
