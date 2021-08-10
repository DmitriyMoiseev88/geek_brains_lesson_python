# names = ('Иван', 'Николай', 'Сергей', 'Петр', 'Саша')
# surnames = ('Иванов', 'Николаев', 'Сергеев', 'Петров')

# for name, surname in zip(names, surnames):
#     print(f'{name} {surname}')

# for index, name in enumerate(names, 1):
# print(f'{index} {name}')
# print(list(enumerate(names, 1)))# Список из картежей
# в картеже пара (2, 'Сергей')
# for index, name in list(enumerate(names, 1)):
# print(index, name)
# '''
#  Из указанной коллекции names, возваращает
#  значение с порядковым номером. Вторым аргументом можно указать старт нумерации
#  третий параметр - это шаг (names, 1, 6), колличество арг должно ровнятся кол переменн
#  в цикле for
# '''

# Тема занятия - функции.
# '''
# Создвем фукции для кода из занятия №1. Для кол-ва запросов (спортсменов)
# больше, чем 1.
# '''
# a = int(input('Результат спортсмена в первый день: '))
# b = int(input('Желаемая дистанция: '))
# days = 1
# while a < b:
# a *=1.1
# days += 1

# print(f'Спортсмен достигнет дистанции в {b} км за {days} дней')

# def sport_result(a, b):# Если a=2 при обьявлении, это значение по умолчанию
# Они ставятся в коце, с начала позиционные
# При вызовве можно его не передавать sport_result(a-не указ, b=5)
# Именнын можно переопределить при вызове фун.
# days = 1
# while a < b:
# a *= 1.1
# days += 1

# print(f'Спортсмен достигнет дистанции в {b} км за {days} дней')

# sport_result(2, 3)# Такая передача арг позиционная
# т.к. 2 передается в a, 3 в b - порядок важен.
# Если при вызове функции передать a=2, b=3. Это именные арг,
# их можно менять местами
# Пользователь может указать свое значение и при наличии знач по умолчаню,
# оно перезапишится

# """ Для большого количества арг используется распаковка. при ихпередачи в функ.
# используется *args - для обозначения позиц. арг
# """


#def sport_result(*args):
    #print(args)  # - выдаст картеж, т.к. каждая позиция арг. важна
    #a, b = args  # так распоковали картеж в вперемен
# Если позиц арг. больше перемен. то *с - как перемен. заберет картеж остальных арг.
# a = args[0] Распаковка по индексу, что бы проигнорировать
# b = args[1] оставшиеся арг.

# sport_result(a=2, b=3, c=5, d=43, e=24) Если именнованных арг.
# много - мы используем для распаековки **kwargs
# def sport_result(**kwargs):
    # print(kwargs) - вы даст словарь {'a': 2, 'b': 3, ...}
    # Ключ словаря - имя переменной
    # a = kwargs['a'] для распаковки обращввемся к ключчу
    # b = kwargs['b']

# sport_result(2, 5, b=3, c=5, d=43, e=24) При смешанной передаче - с начала указ.
# позиц. арг, потом именнов
# def sport_result(*args, **kwargs):
    # print(args) - кортеж
    # print(kwargs) - словарь
# sport_result(2, 5, b=3, c=[1, 2, 3, 5], d=43, e=24) и так можно

        #return b, days

#result = sport_result(2, 5)
#print(*result)

# return - оператор того, что функция считала и, что должна вернуть
# указываем что она возврашавет (return b, days)
# result = sport_result(2, 5) - Должны этот результат принять, обьявление
# через запятую - это создание картежа
# Если не указать возвращемых значений, вернет Non. Так же будет если не указать return
# print(result)

#my_list = [3, 5, 1, 2] # Изменяемый тип, не имеет встроенный return
#print(type(my_list))
#my_list.sort() # Сразу меняет лист, ничего не возвращая
#print(my_list)

#my_dict = {1:1, 2:2}
#result = my_dict.get(1)
#print(result)
#
# '''
# Операторов return в функ. может быть несколько
# он как break останавливает действие
# '''
#def sport_result (*args):
    #a, b = args
    #days = 1
    #if a < 0 or b < 0: # аналог break
        #return # = Nan, сработвло условие отрицвтельных чисел
    #while a < b: # Если не будет этого оператора, уйдем в бесконечный цикл
        #a *= 1.1
        #days += 1
    #return b, days

#result = sport_result(-1, -5) # Два оператора, его можно проанализировать
#if result is None:
    #print (f'Введены отрицательные числа')
#print(result)

# Лямбда
#my_func = lambda p1,p2: p1+p2 #функция анонимная
#print(my_func(2, 5))
#print(my_func('abra', 'kadabra')) # Канкотинация сторок

#print((lambda p1,p2: p1+p2)(3, 10))
# Вызов анонимной функ. без перемен.

#new_func = lambda *args: args
#print(new_func(10, 20, 30, 40))# Принтует картеж

#def named_func(param):
    #return param ** 0.5

#print(named_func(100))
# Или так
#square_rt = lambda param: param ** 0.5# Всегда присутствует только одно вырвжение
#print(square_rt(100))

#print('yes') if 5  > 4 else print('no') # Так же lambda функция

# ВСТРОЕННЫЕ ФУНУЦИИ
#my_list = [3 , 45, 243, 1, 443, 3, 4543]
#print(max(my_list))

#my_list = [3 , 45, 243, 243, 243, 243, 1, 1, 1, 443, 3, 4543]
#print(max(my_list, key=my_list.count))# Вычисляем макс из кол-ва повторений

#print(max(my_list, key=lambda x: x%34))# Остаток от деления на 2
#print(max(my_list, key=lambda x: x//5 ))# макс целое цисло от деления

# Функция Range - это генератор чисел
#print(list(range(7))) # Диапозон 0 -7 (0 - 6 - последнее число не вкл)
#print(list(range(2, 8)))# Диапозон 2 - 8
#for i in range(5, 34, 8):
    #print(i)
#print(list(range(1, 9, 2))) # Диапозон + шаг в 2
#print(list(range(1, -7, -2)))# Диапозон + шаг в -2
#print(list(range(1, 0)))# Диапозон 1 - 0 - это пуст. список

#for el in range(4, 20, 4):
    #res = el / 2
    #print(f'Результат деления {el} на 2: {int(res)}')

# Зона видимости переменных
# '''Переменные a и b находятся в нутри функции'''
# def sport_result (*args):
#     global a
#     a, b = args # В области видимости в не функции фунуции
#     days = 1
#     if a < 0 or b < 0: # аналог break
#         return # = Nan, сработвло условие отрицвтельных чисел
#     while a < b: # Если не будет этого оператора, уйдем в бесконечный цикл
#         a *= 1.1
#         days += 1
#     return b, days # Ее видно в не функции
#
# result = sport_result(-1, -5) # Два оператора, его можно проанализировать
# if result is None:
#     print (f'Введены отрицательные числа')
# print(result)
# print(a) # Будет ошибка, если не сделать переменную глобальной
# # т.к. она в не функ. объявлена
#
# # НЕ ЛОКАЛЬНЫЕ ЗОНЫ ВИДИМОСТИ
# def ext_func():
#     """Функция что-то считает."""# Однострочный комм.
#     my_var = 0 # это перемен объявлена внешей функ. она локальна для ext_func
#     def int_func():
#         nonlocal my_var # для внутрен. функ. перемен. не локал
#         my_var += 1
#         return my_var
#     """Возвращает вычисления, полученные на входе.
#
#     Внимение на:
#     переменную во внешней функции
#     во внутренней - объявить не локал.
#     """
#     return int_func
#
# func_obj = ext_func()
# print(func_obj)
# print(func_obj())
# print(func_obj())
# print(func_obj())

# '''Документирование кода'''
#
# '''Разбор д/з от 2го занятия
# 1. Создать список и заполнить его эллементами различных
# типоа данных. Реализовать скрипт проаерки типа данных
# каждого эллемента. Использовать type() для проверки типа.
# Эллементы типа можно не запрашивать у пользователя, указать
# явно в программе.
# # '''
# my_list = [1, 'a', (1, 2, 3), {'Jun': 6, 'Jul': 7, 'Aug': 8}, [1, 2, 3], set([1, 2, 3])]
# for element in my_list:
#      print(type(element))

# """
# 2. Для списка реализовать обмен значений соседних эллементоая,
# т.е. Значениями обмениваются эллементы с индексами 0 и 1, 2 и 3, итд.
# При не четном кол-ве эллементов последний сохранить на своем месте
# Для заполнения списка эллементов необходимо использовать функции input()
# """
# input_list = input("Введите через пробел эллементы списка: ")
# input_list = input_list.split()
# input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for index in range(0, len(input_list)-1, 2):
#     input_list[index], input_list[index+1] = input_list[index+1], input_list[index]
#
# print(input_list)

# Или так
# result_list = []
# for element in input_list[::2]:
#     index = input_list.index(element)
#     if index+1 == len(input_list):
#         result_list.append(element)
#     else:
#         first_element, second_element = input_list[index], input_list[index+1]
#         result_list.extend([second_element, first_element])
#
# print(result_list)

# """
# 3. Создание словаря
# """
# try:
#     number_of_month = int(input("Введите номер месяца числом от 1 до 12: "))
# except ValueError:
#     print("Неверно введен номер месяцв")
# else:
    # winter = [12, 1, 2]
    # spring = [3, 4, 5]
    # summer = [6, 7, 8]
    # autumn = [9, 10, 11]
    #
    # if number_of_month in winter:
    #     print("Зима")
    # elif number_of_month in spring:
    #     print("Весна")
    # elif number_of_month in summer:
    #     print("Лето")
    # elif number_of_month in autumn:
    #     print("Осень")
    # else:
    #     print("Время года не определенно")

# """ Создание этого же словаря через dict """
#     seson_dict = {}
#     seson_dict = seson_dict.fromkeys([12, 1, 2], 'Зима')
#     seson_dict.update({}.fromkeys([3, 4, 5], 'Весна'))
#     seson_dict.update({}.fromkeys([6, 7, 8], 'Лето'))
#     seson_dict.update({}.fromkeys([9, 10, 11], 'Осень'))
#
#     for seson_month_number, seson in seson_dict.items():
#         if number_of_month == seson_month_number:
#             print (seson)
#             break
#     else:
#         print('Время года не определено')
# # Тоже самое, без лог. условий. Через метод get
#     print(seson_dict.get(number_of_month, 'Время года не определено'))

# """
# 4.  Пользователь вводит строку из нескольких слов, разделленных пробелом
#     Вывести каждое слово с новой строки. Строки нужно пронумировать
#     Если слово длинное, выыодить только первые 10 букв
# """
#
# input_string = input("Введите строку из нескольких слов")
# input_words = input_string.split()
#
# for index, word in enumerate(input_words, 1):
#     print(index, word[:10])

# """
# 5. Реализовать структуру 'Рейтинг', пердставляюший собой набор натуральных чисел.
#     У пользователя необходимо запрашивать новый эллемент рейтинга. Если в рейтинге
#     существуют эллементы с одинаковыми значениями, то новый эллемент с тем же значением
#     должен разместиться после них
# """
#
# my_rating_list = [7, 5, 3, 3, 2]
# my_rating_list_copy = my_rating_list_copy() # копия для изменения списка
#
# new_rating = int(input("Введите новый эллемент рейтнга"))
# try:
#     if new_rating > my_rating_list[0]:
#         my_rating_list_copy.insert(0, new_rating)
#     elif new_rating < my_rating_list[-1]:
#         my_rating_list_copy.append(new_rating)
#     else:
#         for rating in my_rating_list:
#             if new_rating == rating:
#                 rating_index = my_rating_list.index(rating)
#                 rating_count = my_rating_list.count(rating)
#                 new_rating_index = rating_index + rating_count
#                 my_rating_list_copy.insert(new_rating_index, new_rating)
#                 break
#             elif new_rating > rating:
#                 my_rating_list_copy.insert(my_rating_list.index(rating), new_rating)
#                 break
#             else:
#                 continue
#
# except IndexError:
#     print('Неверные вводные данные')
#
# print(my_rating_list_copy)
#
# """
# 6. *Разделить структуру данных "Товары". Она должна представлять собой список картежей.
#     Каждый картеж хранит информацию об отдельном товаре.
#     В картеже два эллемента - номер товара и словарь с параметрами
#     (характеристики товара: название, цена, кол -во, единица изменения).
#     Структуру нужно сформировать програмно, т.е. запрашивать все данные у пользателя.
# """
# my_struct = []
# while True:
#     check_inputs = input(("Продолжить ввод y/n: "))
#     if check_inputs == 'y':
#         my_dict = dict({'название': input('Введите название товара: '), 'цена': input('Введите цену товара: '),
#                         'колличество': input('Введите колличство товара: '), 'ед': input('Введите единицу измерения: ')})
#         my_struct.append((len(my_struct)+1, my_dict))
#     elif check_inputs == 'n':
#         break
#     else:
#         check_inputs = input("Продолжить ввод y/n: ")
# print(my_struct)

# Аналитика о товарах
from typing import Dict, List, Tuple, Union
#
# my_struct_list = [
#     (1, {"название": "компьютер", "цена": 20000, "колличество": 5, "ед": "шт."}),
#     (2, {"название": "принтер", "цена": 6000, "колличество": 2, "ед": "шт."}),
#     (3, {"название": "сканер", "цена": 2000, "колличество": 7, "ед": "упак."})
# ]
#
# my_result_dict = {}
#
# for structure in my_struct_list:# Каждый раз получаем картеж
#     struct_number, struct_info_dict = structure#распаковка картежа, в первую перемен.-номер. Во 2ой - словарь
#     for key, value in struct_info_dict.items():
#         value_list = my_struct_list.get(key, [])
#         if value not in value_list:
#             value_list.append(value)
#         my_result_dict[key] = value_list
#
# print(my_result_dict)


