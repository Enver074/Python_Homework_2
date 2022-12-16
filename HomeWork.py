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

a = input("Введите число: ")
sum = 0 
for i in a:
    if i.isdigit():
        sum += int(i)

print(sum)