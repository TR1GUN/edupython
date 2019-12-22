import xlrd
# Открываем нужную таблицу
def open_book():
    # Открываем нужный нам файл и лист
    book = xlrd.open_workbook('C:/Laba1.xlsx')
    list = book.sheet_by_index(0)
    print("///")
    return list
# проверяем открыли или нет
def open_true_or_false():
    if (open_book() != None):
        open_tabble = True
        print("Таблица успешно открыта")
    else:
        open_tabble = False
        print( "Таблицу не удалось открыть")
    return open_tabble;
