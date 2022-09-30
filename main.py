#Task1 напишите программу которая принимает на вход цифру,
# обозначающую день недели,и проверяет,является ли этот день выходным.
print('Task1'+'\n')
day = int(input('Enter day number'))
if day >7 or day <1:
    print('Please repeatthe input')
elif day ==6 or day==7:
    print("Yes, it's weekend!")
else:
    print("No, it's not weekend!")

#Task1.1 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('Task1.1'+'\n')
def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")

#Task 2 Напишите программу, которая принимает на вход координаты точки (X и Y),
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример: - x=34; y=-30 -> 4 - x=2; y=4-> 1 - x=-34; y=-30 -> 3

print('Task2'+'\n')
def inputCoordinates(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                is_OK = True
                if a[i] == 0:
                    is_OK = False
                    print("Координата не должно быть равна 0 ")
            except ValueError:
                print("Ты ошибся. Вводить надо числа!")
    return a


def checkCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")


koordinate = inputCoordinates(2)
checkCoordinates(koordinate)

#Task3 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print('Task3'+'\n')
n = int(input('input quarter number'))
if n<1 or n>4:
    print('Please, repeat the input')
elif n==1:
    print('x>0 and y>0')
elif n ==2:
    print('x<0 and y>0')
elif n==3:
    print('x<0 and y<0')
elif n==4:
    print('x>0 and y<0')

#Task4 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
print('Task4'+'\n')
print('Enter coordinates point A:')
Ax = float(input('X: '))
Ay = float(input('Y: '))
print('Enter coordinates point B:')
Bx = float(input('X: '))
By = float(input('Y: '))
from math import sqrt
print('Distance between A and B: ',round(sqrt(Ax-Bx)**2+(Ay-By)**2),2)