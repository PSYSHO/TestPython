import student as st
import lecture as lect


def option():
    print("\nВас приветствует программа мониторинга процессов обучения студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть класс  и место которое занимает  студент \n \
    3: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        Surn = str(input("Введите фамилию ученика: "))
        if Surn in st.students['Фамилия']:
            index = st.students['Фамилия'].index(Surn)
        print(f"{st.students['ID'][index]}, {st.students['Имя'][index]},{st.students['Фамилия'][index]}\n,{st.students['Дата рождения'][index]}, {st.students['Успеваемость'][index]}")
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

    elif ch == 2:
        c = input('Введите ID студента для вывода по классам: ')
        if c in lect.lecture['ID']:
            index = lect.lecture['ID'].index(c)
            print(f" Сидит в классе - {lect.lecture['Предмет'][index]}\n\, за партой номер - {lect.lecture['Номер парты'][index]}, это {lect.lecture['Ряд'][index]}, парта - {lect.lecture['Вид парты'][index]}, Имя: {st.students['Имя'][index]}, Фамилия - {st.students['Фамилия'][index]}, и успеваемасть у студента: {st.students['Успеваемость'][index]}")
            print('\nХотите выполнить другую операцию??? Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                option()
            exit()
    else:
        print('еще раз')
    exit()


option()