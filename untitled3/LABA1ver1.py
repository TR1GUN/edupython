import open
import  main_menu
#Открываем нужный нам файл и лист
print("Открываем книгу....")
list = open.open_book()
open_tabble = open.open_true_or_false()

# Вызываем Меню
main_menu.menu(open_tabble)




#--------------------------------------------------------------------------------------------------------------
# book = xlrd.open_workbook('C:/Laba1.xlsx')
# list = book.sheet_by_index(0)
# open_tabble = True
# stroka=23
# stolbetz=2
# # Поставить заглушку - Заменить на метод определения максимальной строки таблицы
# max_stroka = 11360
# # value = list.row_values(stroka)[stolbetz]
# # value1 = list.cell(stroka, stolbetz).value
# # print(value)
# # print(type(value))
# # print(value1)
# # print(type(value1))
