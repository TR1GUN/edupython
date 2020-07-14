# --------------------------------------Задание 1-------------------------------------------------------------------------
# Написать функцию, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
# 4 варианта решения - выстроены по количеству выделяемой памяти

# Способ первый - все составные числа получаются из умножения простых. Проверяем все простые числа на деление по модулю
# Имеет смысл когда диапазон четко задан, есть желание писать много кода и нет ресурсов памяти:

def function_find_out_on_prime_number_vol_1(number):
    # Для начала выясняем входит ли данное число в заданный диапазон
    if 0 < number < 1000:
        try:
            # для начала отметаем все ЧЕТНЫЕ числа кроме 2, так как они являются априори составными
            def find_even_numbers(number):
                # отметаем двойку
                if number == 2:
                    result = True
                else:
                    # Теперь отметаем все четные числа:
                    if number % 2 == 0:
                        result = False
                    else:
                        # Иначе - оставляем не определенным тип
                        result = None
                return result
            # Теперь надо отсеять все числа полученные из простых чисел до 31. 32 квадрат - 1024.
            # Нам нужны числа: 3, 5 , 7 , 11 , 13 ,17, 19, 23, 29, 31
            def find_division_by_3(number):
                if number % 3 == 0:
                    result = False
                else:
                    # Иначе - оставляем не определенным тип
                    result = None
                return result

            def find_division_by_5(number):
                if number % 5 == 0:
                    result = False
                else:
                    # Иначе - оставляем не определенным тип
                    result = None
                return result

            def find_division_by_7(number):
                if number % 7 == 0:
                    result = False
                else:
                    # Иначе - оставляем не определенным тип
                    result = None
                return result

            def find_division_by_11(number):
                if number % 11 == 0:
                    result = False
                else:
                    # Иначе - оставляем не определенным тип
                    result = None
                return result

            def find_division_by_13(number):
                if number % 13 == 0:
                    result = False
                else:
                    # Иначе - оставляем не определенным тип
                    result = None
                return result

            def find_division_by_17(number):
                if number % 17 == 0:
                    result = False
                else:
                    # Иначе - оставляем не определенным тип
                    result = None
                return result

            def find_division_by_19(number):
                if number % 19 == 0:
                    result = False
                else:
                    # Иначе - оставляем не определенным тип
                    result = None
                return result

            def find_division_by_23(number):
                if number % 23 == 0:
                    result = False
                else:
                    # Иначе - оставляем не определенным тип
                    result = None
                return result

            def find_division_by_29(number):
                if number % 29 == 0:
                    result = False
                else:
                    # Иначе - оставляем не определенным тип
                    result = None
                return result

            def find_division_by_31(number):
                if number % 31 == 0:
                    result = False
                else:
                    # Иначе - оставляем не определенным тип
                    result = None
                return result

# Применяем наши функции:
            result = find_even_numbers(number)
            # Если наше число нечетное:
            if result == None:
# Важный момент - если полученное число равно числу, на которое проверяем - надо сразу выставить True
                if number in [3 , 5 , 7, 11 , 13 ,17, 19, 23, 29, 31 ] :
                    result = True
                else:
                    result = find_division_by_3(number)
                    if result == None:
                        result = find_division_by_5(number)
                        if result == None:
                            result = find_division_by_7(number)
                            if result == None:
                                result = find_division_by_11(number)
                                if result == None:
                                    result = find_division_by_13(number)
                                    if result == None:
                                        result = find_division_by_17(number)
                                        if result == None:
                                            result = find_division_by_19(number)
                                            if result == None:
                                                result = find_division_by_23(number)
                                                if result == None:
                                                    result = find_division_by_29(number)
                                                    if result == None:
                                                        result = find_division_by_31(number)
                                                        if result == None:
                                                            result = True

        except:
            print()
        finally:
            print(result)
            return result
    else:
        print('Число не входит в нужный диапазон')


# Способ второй - Решето Эрастосфена - Получаем массив всех чисел от 1 до 1000 с нужными нам значениями, после вытаскиваем нужное значение по индексу
def function_find_out_on_prime_number_vol_2(number):
    # Формируем список чисел через решето :
    def sieve_Erastofen():
        sieve = [True] * (1001)
        # Начинаем перебирать цифры от двойки которые четные :
        for x in range(2, 1001):
            if sieve[x]:
                # Убираем числа, которые делятся на х
                for i in range(2 * x, 1001, x):
                    sieve[i] = False
        return sieve;
    sieve = sieve_Erastofen() ;
    # После чего делаем уточнения значений для двойки и нуля
    sieve[0] = False
    sieve[1] = False
    # Получаем результат по индексу
    if 0 < number < 1000:
        result = sieve[number]
        return result
    else:
        print('Число не входит в нужный диапазон')

# Способ третий - перебор всех значений до первого делителя - иногда очень затратный, так как на него требуется больше памяти. - как следствие - самый долгий.
def function_find_out_on_prime_number_vol_3(number):
    if 0 < number < 1000:
        if number == 1:
            return False
        for x in range(2, 1000):
            if number % x == 0:
                return False
        else:
            return True
    else:
        print('Число не входит в нужный диапазон')
# Способ четвертый и ультимативный - не надо изобретать велосипед. Если вам надо что-то написать - подумайте не написано ли было это до вас:
# импортируем для этого нужную библиотеку
import sympy
def function_find_out_on_prime_number_vol_4(number):
# Генерируем список , который уже содержит простые числа из заданного диапазона !!
    prime_number = list(sympy.primerange(0, 1000))
    if number in prime_number:
        result = True
    else :
        result = False
    return result
# ----------------------------------------------------------------------------------------------------------------
# Необходимо разработать скрипт, который будет выводить все записи из лог-файла «/var/log/messages», у которых временная метка находится в заданном диапазоне.
# для начала напишем функцию для ввода даты
def input_start_date():
    date_start = {}
    print('Ввсести месяц - начальное значение')
    date_start['month'] = input()
    print('Ввсести день - начальное значение')
    date_start['day']  = input()
    print('Ввсести час - начальное значение')
    date_start['hour']  = input()
    print('Ввсести минуту - начальное значение')
    date_start['minute']  = input()
    print('Ввсести секунду - начальное значение')
    date_start['second']  = input()
    return date_start

def input_finish_date():
    date_finish = {}
    print('Ввсести месяц - конечное значение')
    date_finish['month'] = input()
    print('Ввсести день - конечное значение')
    date_finish['day']  = input()
    print('Ввсести час - конечное значение')
    date_finish['hour']  = input()
    print('Ввсести минуту - конечное значение')
    date_finish['minute']  = input()
    print('Ввсести секунду - конечное значение')
    date_finish['second']  = input()
    return date_finish
#
# Получаем два списка - начальная дата , конечная дата

# Функция для чтения файла , и возвращения его в качестве строки
def read_file():
# Вводим путь
    path = '/var/log/messages'
# # открываем файл
    file = open(path, 'r')
    return file

# для начала напишем счетчик который будет прибавлять по одной секунде к нужному нам времени:
def add_ONE_second_to_date(date):
    date['second'] = date['second'] + 1
    if date['second'] > 60:
        date['second'] = 0
        date['minute'] = date['minute'] + 1
    if date['minute'] > 60:
        date['minute'] = 0
        date['hour'] = date['hour'] + 1
    if date['hour'] > 60:
        date['hour'] = 0
        date['day'] = date['day'] + 1
    if date['day'] > 31:
        date['day'] = 1
        date['month'] = date['month'] + 1
    return date
# теперь приводим список к виду строки :
# Добавляем ноль и переводим в строку:
def adding_zero(number):
    if number < 10 :
        number_string = '0' + str(number)
    else:
        number_string = str(number)
    return number_string


# Указываем Правильно месяц
def indicate_month(month_number):
    # Делаем список из месяцев
    month = ['None', 'Jun ', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if month_number < 13:
        if month_number > 0:
            month_string = month[month_number]
    else:
        month_string = month[0]
    return month_string;

# Теперь делаем преобразования:
def dict_on_string(date_dict):
    second = adding_zero(date_dict['second'])
    minute = adding_zero(date_dict['minute'])
    hour = adding_zero(date_dict['hour'])
    day = adding_zero(date_dict['day'])
    month = indicate_month(date_dict['month'])
    string_date = month + " " + day + " " + hour + ":" + minute + ":" + second
    return string_date



#  ищем по индексу первое вхождение подстроки в строке
def find_entry(date_dict, string_log):
    bool_date_log = None
    # Сначала ищем первую дату от нужной нам
    while bool_date_log != True:
        date = dict_on_string(date_dict)
        if date in string_log :
            bool_date_log = True
        else:
            date_dict = add_ONE_second_to_date(date_dict)
    index = string_log.index(date)
    return index

# а теперь финальная функция :
def search_log_by_date_vol_1():
    # Получаем входную и выходную дату
    start_date_dict = input_start_date()
    finish_date_dict = input_finish_date()
    # Получаем строкой сам лог линукса
    string_log = read_file()
    # Получаем входной индекс:
    index_input = find_entry(start_date_dict, string_log)
    # Получаем выходной индекс
    index_output = find_entry(finish_date_dict, string_log)
    # А Теперь нарезаем нашу строку :
    string_final = string_log[index_input:index_output]
    print(string_final)
    return string_final




# ----------------------------------------------------------------------------------------------------------------
# Задано число m, нужно написать функцию, которая выведет на экран числа от m до 0.
# Важное условие - нельзя использовать никакие циклы, условные операторы, тернарные операторы и так далее.
#
#  функция рандж и массивы:
def getting_in_range(n):
    n = n + 1
    # получем массив котрорый содержит все значения от 0 до нужного значения по возрастанию
    list_range = list(reversed(range(0, n)))
    # а теперь все элементы массива соеденяем в строку
    a = str(','.join(map(str,list_range)))
    print(a)

