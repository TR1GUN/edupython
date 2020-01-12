# Напишем простой скрипт для подгонки в SQL таблицу

import csv
import random
import time
# Открырваем файл
CSV_File = open('Laba1.csv')
CSV_File_Reader = csv.reader(CSV_File, delimiter = ';' )


# Делаем из него Список
CSV_File_list = list(CSV_File_Reader)

# "Чистим"  столбцы с годом (6) и страницами (7) и ценой (10)
for row in range(len(CSV_File_list)):
    # Отчищаем от лишнего
    # вспомогательные функции для работы со столбцами
    def checking_empty_string(x, y):
        if x is '' :
            print('Значение Пустое')
            x = y


        return x;

    def year_6(x):
        revised = x[:4]
        return revised ;

    def pages_7(x):
        try:
            x.slip(str='',count=2)
            revised = int(x[0])
        except:
            revised = x[:3]
        return revised;
    def price_10(x):
        try :
            revised = int(x)
        except:
            revised = 4000
        return revised;


    # Оригинальные значения
    values_before_change = [CSV_File_list[row][6] , CSV_File_list[row][7] ,CSV_File_list[row][10] ]
    # Заменяем значения
    CSV_File_list[row][6] = checking_empty_string(year_6(values_before_change[0]), random.randint(1950,2000))
    CSV_File_list[row][7] = checking_empty_string(pages_7(values_before_change[1]), random.randint(50,150))
    CSV_File_list[row][10] = checking_empty_string( price_10(values_before_change[2]) , random.randint(50,100))
    ID_number = row
    CSV_File_list[row].append(ID_number+1)
    # проверяем нулевые значения , исправляем

    if CSV_File_list[row][10] is '':
        print('Пустое значение')
        time.sleep(10000)

    if CSV_File_list[row][7] is '':
        print('Пустое значение')
        time.sleep(10000)

    if CSV_File_list[row][6] is '':
        print('Пустое значение')
        time.sleep(10000)

# Проверяем наличие в строке символа точки с запятой , и если она там то заменяем ее
    for semicolon in range(len(CSV_File_list[row])):

        try:
            if ';' in CSV_File_list[row][semicolon] :
                semicolon_original = CSV_File_list[row][semicolon]
                CSV_File_list[row][semicolon] = semicolon_original.replace(';', ':')

        except :
            print("Строка не строка")



    print(CSV_File_list[row])
CSV_File.close()
# Записываем
# Создаем нужный файл
CSV_File_write = open('Books.csv', 'w', newline = '')
CSV_Writer = csv.writer(CSV_File_write, delimiter = ';')

for row in CSV_File_list:
    CSV_Writer.writerow(row)

# ---------------------------------------------------------------------------------------
#                                 Пользователи
# ---------------------------------------------------------------------------------------

# Генерируем Имена
users_library_file = open('test.txt').read()
users_library_n = users_library_file.split()
users_library = []

# Добавляем Необходимые столбцы
i = 0
number_library_card = 10000
ID_users = 0
while i < len(users_library_n):
    users_fio = []
    users_fio.append(users_library_n[i])
    users_fio.append(users_library_n[i+1])
    users_fio.append(users_library_n[i+2])
    number_library_card = number_library_card +1
    ID_users = ID_users + 1
    users_fio.append(number_library_card)
    users_fio.append(ID_users)
    users_library.append(users_fio)
    del users_fio
    i = i + 3
# Сохраняем в нужный файл
# пам пам

users_library_File = open('users_library.csv', 'w', newline = '')
users_library_Writer = csv.writer(users_library_File, delimiter = ';')
for row in users_library:
    users_library_Writer.writerow(row)
users_library_File.close()
print(users_library)

# ---------------------------------------------------------------------------------------
#                                 Состояние Книги
# ---------------------------------------------------------------------------------------
# Создадим Таблицу состояния книги

Book_status = []
Book_status_constructor_list = []
Book_status_constructor = {}

# Стеллаж-Полка-Номер
Rack = 1
Shelf = 1
Number = 0


for x in range(11361):
    Book_status_constructor['ID_Books'] = x +1
    Number = Number + 1
    if Number > 30 :
        Number = 1
        Book_status_constructor['Number'] = Number
        Shelf  = Shelf + 1
        if Shelf > 7 :
            Shelf = 1
            Book_status_constructor['Shelf'] = Shelf
            Rack = Rack + 1
            Book_status_constructor['Rack'] = Rack


        else:
            Book_status_constructor['Shelf'] = Shelf + 1
            Book_status_constructor['Rack'] = Rack + 1

    else:
        Book_status_constructor['Number'] = Number
        Book_status_constructor['Rack'] = Rack
        Book_status_constructor['Shelf'] = Shelf

    Book_status_constructor['presence'] = True
    Book_status_constructor['Books_primary_key'] = x +1


    Book_status_constructor_list = [Book_status_constructor['ID_Books'], Book_status_constructor['Rack'] ,Book_status_constructor['Shelf'],Book_status_constructor['Number'],Book_status_constructor['presence'],Book_status_constructor['Books_primary_key']]
    Book_status.append(Book_status_constructor_list)

Book_status_File = open('Book_status.csv', 'w', newline = '')
Book_status_writer = csv.writer(Book_status_File, delimiter = ';')


for row in Book_status:
    Book_status_writer.writerow(row)

Book_status_File.close()

# ---------------------------------------------------------------------------------------
#                                 Состояние Книги
# ---------------------------------------------------------------------------------------