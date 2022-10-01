print('Task1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр')
float_num = input('input float number: ')
print(type(float_num))
sum = 0
for i in float_num:
    if i != '.':
        sum += int(i)

print(sum)

print('Task2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')
number = int(input('input N: '))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
    print(factorial)

print('Task3 Задайте список из n чисел последовательности $(1+\\frac 1 n)^n$ и выведите на экран их сумму.')
number = int(input('Enter number: '))


def sequence(num):
    return [round((1 + 1 / x) ** x, 2) for x in range(1, num + 1)]


print(sequence(number))
#print(round(sum(sequence(number))))

print('Task4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.')
import random
N = int(input('Введите число'))
numbers = []
for i in range(N):
    numbers.append(random.randint(-N, N + 1))

print(numbers)
print(numbers[1] * numbers[3])

file = open('file.txt', 'w')
while True:
    s = input('Укажите позицию для вычисления - ')
    if s == "":
        break
    file.write(s + "\n")
file.close()

result = 1
file = open('file.txt', 'r')
for line in file:
    if line == "":
        break
    result *= numbers[int(line)]
file.close()
print(result)

print('Task5 Реализуйте алгоритм перемешивания списка.')
lst = [random.randint(0,10) for i in range(random.randint(5,20))]
print(f"исходный список:\n {lst}")
random.shuffle(lst)
print(f"список после перемешивания:\n{lst}")