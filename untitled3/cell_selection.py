import LABA1ver1

# Осуществляем поиск по таблице
# Столбцы:
# 0 - хз что
# 1 - Автор!!
# 2 - Название книги!!
# 3 - Перевод\Составитель
# 4 - Город издания
# 5 - Издательство
# 6 - Год издания !!
# 7 - Колличество страниц!!
# 8 - Переплет
# 9 - Тип книги
# 10 - Номинальная Цена
# 11 - Описание
# 12 - Состояние

# поиск по авторам
def cell_selection1(avtor):
    value = LABA1ver1.list.cell(avtor, 1).value
    value = str(value)
    return value

# поиск по названию
def cell_selection2(name):
    value = LABA1ver1.list.cell(name, 2).value
    value = str(value)
    return value

# поиск переводу\составителю
def cell_selection3(avtor_translate):
    value = LABA1ver1.list.cell(avtor_translate, 3).value
    value = str(value)
    return value

#Поиск по городу
def cell_selection4(city):
    value = LABA1ver1.list.cell(city, 4).value
    value = str(value)
    if (value == "М."):
        value = "Москва"
    elif (value == 'Л.' ):
        value = "Санкт- Питербург"
    return value
# Поиск по издатльству
#поиск ячеек по году издания
def cell_selection6(year):
    value = LABA1ver1.list.cell(year, 6).value
    value = int(value)
    return value

#Колличество страниц
def cell_selection7(page):
    value = LABA1ver1.list.cell(page, 7).value
    value = str(value)
    s = value.split(maxsplit=-1)
    value1 = s[0]
    value1 = int(value1)
    return value1
# Поиск по переплету
# Поиск по Тип книги

# Поиск по номинальной цене