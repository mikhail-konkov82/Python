#Задача №3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
some_list = []
n = int(input("введите n = "))
for i in range(1, n+1):
    some_list.append(round(((1+(1/i))**i), 3))
print(some_list)