import csv
from userInterface import get_info

info = get_info()
def writing_scv ():
    with open ('Phonebook.csv', 'a',encoding='UTF8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_txt ():
    with open ('Phonebook.txt', 'a',encoding='UTF8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')