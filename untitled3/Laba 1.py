# Подключаем нужные библиотеки
# Бибиолиотека для  Excel
import xlrd

#Открываем нужный нам файл и лист
book = xlrd.open_workbook('C:/Laba1.xlsx')
list = book.sheet_by_index(0)
stroka=0
stolbetz=0
# Поставить заглушку - Максимальное знанчение ячеек таблицы
max_stroka = 11360

# Выбор параметра работы
print("Выбирите параметры работы\n1 - Поиск по всей таблице\n2 - Поиск по авторам\n3 - Поиск по Названию\n4 - Поиск по серии \n5 - Поиск по городу\n6 - Поиск по издательству \n7 - Поиск по году\n8 - Поиск по колличеству страниц\n9 - Поиск по описанию к книги ")
# 1 - Поиск по всей таблице
# 2 - Поиск по авторам
# 3 - Поиск по Названию
# 4 - Поиск по серии
# 5 - Поиск по городу
# 6 - Поиск по издательству
# 7 - Поиск по году
# 8 - Поиск по колличеству страниц
# 9 - Поиск по описанию к книги






















search_selection = input()
int(search_selection)
if search_selection == 1:
    print("Введите то, что хотите найти")
    search = input()

elif search_selection == 2:
    print("Введите то, что хотите найти")
    search = input()
    search_avtor(search)
elif search_selection == 3:
    print("Введите то, что хотите найти")
    search = input()
    search_name(search)
elif search_selection == 4:
    print("Введите то, что хотите найти")
    search = input()
    search_serial(search)
elif search_selection == 5:
    print("Введите то, что хотите найти")
    search = input()
    search_city(search)
elif search_selection == 6:
    print("Введите то, что хотите найти")
    search = input()
    search_izdatel(search)
elif search_selection == 7:
    print("Введите то, что хотите найти")
    search = input()
    search_year(search)
elif search_selection == 8:
    print("Введите то, что хотите найти")
    search = input()
    search_str(search)
elif search_selection == 9:
    print("Введите то, что хотите найти")
    search = input()
    search_opisanie(search)
else:
    print("Вы не выбрали ни одного правильного параметра")
#----------------------------------------------------------------------------------------------------------------------
# Функции для параметров
# Поиск авторам
def search_avtor(x):
    stolbetz = 1
    while stroka < max_stroka :
        value = list.row_values(stroka)[stolbetz];
        str(value)
        if x in value:
            print(value)
        stroka =+1

def search_name(x):
    stolbetz = 2
    while stroka < max_stroka :
        value = list.row_values(stroka)[stolbetz];
        str(value)
        if x in value:
            print(value)
        stroka =+1

def search_serial(x):
    stolbetz = 3
    while stroka < max_stroka :
        value = list.row_values(stroka)[stolbetz];
        str(value)
        if x in value:
            print(value)
        stroka =+1

def search_city(x):
    stolbetz = 4
    while stroka < max_stroka :
        value = list.row_values(stroka)[stolbetz];
        str(value)
        if x in value:
            print(value)
        stroka =+1

def search_izdatel(x):
    stolbetz = 5
    while stroka < max_stroka :
        value = list.row_values(stroka)[stolbetz];
        str(value)
        if x in value:
            print(value)
        stroka =+1

def search_year(x):
    stolbetz = 6
    while stroka < max_stroka :
        value = list.row_values(stroka)[stolbetz];
        str(value)
        if x in value:
            print(value)
        stroka =+1

def search_str(x):
    stolbetz = 7
    while stroka < max_stroka :
        value = list.row_values(stroka)[stolbetz];
        str(value)
        if x in value:
            print(value)
        stroka =+1

def search_opisanie(x):
    stolbetz = 11
    while stroka < max_stroka :
        value = list.row_values(stroka)[stolbetz];
        str(value)
        if x in value:
            print(value)
        stroka =+1