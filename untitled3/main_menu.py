option1 = "Поиск по всей таблице"
option2 =  "Поиск по авторам"
option3 = "Поиск по Названию"
option4 = "Поиск по серии"
option5 = "Поиск по городу"
option6 = "Поиск по издательству"
option7 = "Поиск по году"
option8 = "Поиск по колличеству страниц"
option9 = "Поиск по описанию к книге"
search_opton = "Выбран параметр поиска : "


def menu(x):
    if x == True:
        print ("Вырерите параметр поиска")
        print("\n 1 - Поиск по всей таблице\n 2 - Поиск по авторам\n 3 - Поиск по Названию\n 4 - Поиск по серии\n 5 - Поиск по городу\n 6 - Поиск по издательству\n 7 - Поиск по году\n 8 - Поиск по колличеству страниц\n 9 - Поиск по описанию к книги ")
        option = opton_search(option_selection())
    else:
        print("Лист не найден")

# 1 - Поиск по всей таблице
# 2 - Поиск по авторам
# 3 - Поиск по Названию
# 4 - Поиск по серии
# 5 - Поиск по городу
# 6 - Поиск по издательству
# 7 - Поиск по году
# 8 - Поиск по колличеству страниц
# 9 - Поиск по описанию к книге


# Ввод варианта
def option_selection():
    option_selection = input()
    return option_selection;


def opton_search(x):
    x = int(x)
    if x == 1:
        print(search_opton + option1)
    elif x == 2:
        print(search_opton + option2)
    elif x == 3:
        print(search_opton + option3)
    elif x == 4:
        print(search_opton + option4)
    elif x == 5:
        print(search_opton + option5)
    elif x == 6:
        print(search_opton + option6)
    elif x == 7:
        print(search_opton + option7)
    elif x == 8:
        print( search_opton + option8)
    elif x == 9:
        print( search_opton + option9)
    else:
        print("Не выбранно ни одного параметра поиска")
        x = 1
    return x

