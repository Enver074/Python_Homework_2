# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


# a = float(input("Введите число: "))


# while a != int(a):
#     a *= 10 
    
# sum = 0
# while a > 0:
#     sum += a % 10
#     a //= 10     

# print(int(sum))

# a = input("Введите число: ")
# sum = 0 
# for i in a:
#     if i.isdigit():
#         sum += int(i)

# print(sum)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input("Введите число N: "))

# i = 1
# mult = 1
# print("[", end="")
# while i <= (N-1):
#     mult *= i
#     i += 1
#     print( f'{mult}, ', end = " ")
# print( f'{mult*N}] ', end = " ")

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

# n = int(input("Введите число N: "))
# num = {}
# sum = 0
# for i in range(1, n+1):
#     num[i]=round((1+(1/i))**i, 2)
#     sum += num[i]
# print(num)
# print(sum)


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


N = int(input('Введите число N: '))
a = list(range(-N, N+1))
print(a)
data = open('file.txt', 'r')
position = list(map(int,data.readlines()))
mult = 1
for i in range(len(position)):
    mult *= [i for i in range(-N, N+1)][position[i]]
print(mult)
