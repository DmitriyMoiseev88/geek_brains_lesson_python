# """
# Генераторы
#     содержат идею последовательности и отдают ее.
#     нехранит список, дает по 1му эллем - эффкетивная работа памяти
# """
# def gen():
#     x = 42
#     # выплевывает по одному значению
#     yield x
#     x += 1
#     yield x
#     x += 1
#     yield x
# # g = gen()
# # print(g)
# # print(next(g))
# # print(next(g))
# # print(next(g))
# #print(next(g)) # StopIteration ошибка (next) закончился в теле генератора
#
# for i in gen(): # Умеет обрабатывать ошибку - когда генератору  нечего отдавать
#     print(i)

# """
# Задача на последовательность Фибиначи
# 1 2 3 5 8 13 21 34 55 89 ...
#     -каждый след. эллем - это суммв 2ух предыдущих
# """
# def fibonacci(xterms): #какой длинны последовательность нужно сгенерировать.
#         x1 = 0 # первое условие, что бы сформировать 1
#         x2 = 1
#         count = 0
#         if xterms <= 0:
#             print('укажжите целое число больше 0')
#         elif xterms == 1:
#             print('последовательность Фибоначи до', xterms, ":")
#             print(x1)
#         else:
#             while count < xterms:
#                 xth = x1 + x2
#                 x1 = x2
#                 x2 = xth
#                 count += 1
#                 yield xth
#
# # fib = fibonacci(5)
# # print(next(fib))
# # print(next(fib))
# # print(next(fib))
# # print(next(fib))
# # print(next(fib))
# # цикл дружит с next, что бы не вызывать каждый раз и без ошибок
# for i in fibonacci(14):
#     print(i)

# тернальный оператор
# print('yes') if 5 > 4 else print('no')
#
# # Лямбда
# def sum(x, y):
#     return x+y
#
# print((lambda x, y: x+y)(2, 5)) # Так же можно зписать для функции гененратора

# создаем список
# alist = [4, 16, 64, 256]
# # вычисляем квадратный корень, используя выражения генератора
# out = [a**(1/2) for a in alist if a == 4]
# # записанно условие которое нужно сделать с эллем.a**(1/2)
# # + выражение цикла for a in alist -каждый эллем. исходного списка возвожу в степень 1/2 - это вычисление квадрата
# # [2.0, 4.0, 8.0, 16.0] - вычислился квадрат из каждого эллем.
# # + условие if a  == 4 вычисляем кв.корень только того эллем, который тождественно равен 4
# print(out)
#
# out = (a**(1/2) for a in alist) # generator object <genexpr>
# print(out) # это функция выражения генервтора

# input можно помещать в выражения генератора
# out = [int(a)**(1/2) for a in input().split()]
# # int(a)**(1/2) for a - операция с цислом (потому int)
# # in input().split()] - дает строку, разбиваем на список(split() - всегда дает список)

# добавляем в выражение генератора условия
# out = [a**(1/2) if a == 4 else None for a in alist]
# print(out)

# Используем выражение генератора чтобы вычислмть кв.корень
# out = (a**(1/2) for a in alist)
# print(out)
# print(next(out))
# print(next(out))
# print(next(out))
# print(next(out))

# """
# Создание словарей с использованиием генератора
# """
# my_dict = {el: el*2 for el in range(10, 20)}
# print(my_dict)

# Создание множества
# my_set = {el**3 for el in range(5, 10)}
# # В множество попадает эллем. в степени 3
# print(my_set)

# """
# Функция map и filter
#     устаревшее использование, лучше варинты выше
# """
# alist = [4, 16, 64, 256]
# my_map = map(lambda x: x**(1/2), alist)
# print(list(my_map)) # указали в какую конкретную струкуру данных
# создание переменной, хранящей функцию map
# первый арг - функция пременяемвя к каждому арг. последовательности
# второй арг - надор данных, над котором происходят преобразования

# filter - фильтрация, выбор тех объектов которые соответствуют условиям
# my_filter = filter(lambda x: x%2 != 0, range(10)) # переменная для объявления функ.
# первый арг - функция фильтрации
# второй арг - надор данных, сгенерируемая последовательность от 0 до 9 (range(10))
# print(list(my_filter)) # <filter object - потому перевели в конкретную структуру данных

# """
# Встроенные модули
#     random:
#     randint(начало, конец)
#     choice(послдовательность)
#     randrange(начало, конец, шаг)
#     shuffle(после-сть)
#     sample(после-сть, кол-во элл.)
#     gauss(начало, конец)
# """
# import random
# print(random.randint(3, 9)) # случайная целая величина из указанного диапазона
# print(random.randrange(3, 13, 2)) # похож на range, генирится указанный диапозон
# передали шаг, далее из этой последов- сти выбираем вкличину
# print(random.random()*10) # не целые числа, случайную величину от 0 до 1 - float
# * 10 - это увеличение границы числа

# a = [1, 2, 3, 4, 5, 6, 7,] # коллекция в виде списка
# print(random.choice(a)) # случ. выбор велич из имеюшийся послед-сти
# print(random.sample(a, 3)) # несколько случ. величин из списка
# первый арг. - моя коллек.данных
# втор. арг. - колл-во случ. арг. - исходная выборка
# random.shuffle(a) # перемешивание в исходной колл.
# print(a)
# print(random.gauss(0, 1)) # gaussское распределение
#
# from functools import reduce, partial
# """
# Сборник функций высокого уровня: те. функционал. програм.
# взаимодействие с другими функциями или возвращение других функций
#
# reduce(Lambda x, y: x+y, [1, 2, 3, 4, 5,]) вычисляет ((((1+2)+3)+4)+5)
# reduce с начала сложит первые два эллем, потом эту сумму с 3им эллем..
# """
# def my_func(prev_el, el):
#     # prev_el - предыдущ. эллем.
#     # el -текуший эллем.
#     return prev_el + el

# print(reduce(my_func, [10, 20, 30]))
# первый арг - функция над моей колл,
# вторым -  колл.
#
# def my_func_2(param_1, param_2): # модификация моей функции
#     return param_1 ** param_2 # арг. моей функ. не обязательные
# # воъвращает возведение в степень
# new_my_func = partial(my_func_2, 2)
# print(my_func)
# print(new_my_func(4))

# import itertools
# """
# count(start=0, step-1) - возврат равномерно распроделенные переменные
# chain - конкатенирует произвольное число итераторов
# """
#
# for i in itertools.count(0, 2): # от 0 с шагом 2
#     if i >= 10: # обязательно условия выхода
#         break # иначе цикл бесконечен
#     print(i) # в отличии от for in, itertools - генериоет бесконечный набор
#     # count дает равномерно распределенные. целые значения в указанном диапазоне

# count = 0 # счетчик для выхода
# for i in itertools.cycle('ABC'): # бесконечно переберает мою коллекцию
#     if count > 3:
#         break
#     count += 1
#     print(i)

# a = itertools.chain(range(2), range(4, 8))
# for i in a:
#     print(i)

# # декартово произведение
# print(list(itertools.product("ABCD", repeat=2))) # для исследований в комбинатораке

# # все перестановки, которые могут быть для моей коллекции
# print(list(itertools.permutations("ABCD")))

# # сочетания всех эллем. 5- в каком колличесве
# print(list(itertools. permutations("ABCDE", 5)))
#
# # Зацикливание
# progr_lang = ["python", "java", "perl", "javascript"]
# iter = itertools.cycle(progr_lang)
#
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
#
# import math as mt # или from math import ceil, fabs ...
# # округление до целого числа вврх =7
# print(f'ceil() -> {mt.ceil(6.75)}')
# # отдает наибольшее число =4.0. возвращает модуль
# print(f'ceil() -> {mt.fabs(-4)}')
# # возвращает факториал цислп = 120
# print(f'ceil() -> {mt.factorial(5)}')
# # округление до целого числа вних = 4
# print(f'ceil() -> {mt.floor(4.34)}')
# # число бесконечно- Falee или конечно - True
# print(f'ceil() -> {mt.isfinite(10)}')
# # остаток от деления двух цисел = 1
# print(f'ceil() -> {mt.fmod(9, 4)}')
# # возвращает дробну часть = 0.5. и целую = 10.0  от моего числа
# print(f'ceil() -> {mt.modf(10.5)}')
# # = вычисление квадратного корня из числа = 4.0
# print(f'ceil() -> {mt.sqrt(16)}')
# # вычисление синуса
# print(f'ceil() -> {mt.sin(1.5708)}')
# # вычисление косинуса
# print(f'ceil() -> {mt.cos(1.5708)}')
# # вычисление тангенсв
# print(f'ceil() -> {mt.tan(1.5708)}')
# # перевод градусов в радианы
# print(f'ceil() -> {mt.degrees(1.5708)}')
# # перевод радианы в градусы
# print(f'ceil() -> {mt.radians(90)}')




# """разбор домашнего зпдания от 3ей лекции
# 1. Реальзовать функцию, принимающую 2 числа (позиционные апгументы) и выполняющую их деление.
#     Число запрощивать у пользователя, предусмотреть обработку ситуации дклкния на ноль
# """
# def devision(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Произошло деление на ноль"
#     except TypeError:
#         return "Введите дыв числа больше 0"

# print(devision(3, 4))
# print(devision(13, 0))
# print(devision(65, 5))

# """
# 2. Реализовать функцию, принимающую несколтко параметров,
#     описыващих данные пользователя: имя. фамилия, год рождения, город проживания, email, телефон.
#     Принимает параметры как именнованные аргументы.
#     Ревлизовать данные о пользователе одной строкой
# """
# def person_profile(**kwargs):# Формируется в словарь
#     return f"Имя: {kwargs['name']}, Фамилия: {kwargs['surname']}, E-mail: {kwargs['email']}"
#
# print((person_profile(name="Dima", tel="923-584-5260", surname="Moiseev",
#                       birth_year= "1988", city="SPB", email="dmitriy.moiseev.86@gmail.com")))

# """
# 3. Реализовать функцию my_func(), принимающую 3 позиционных аргумента,
#     и возвращающую сумму наибольшую двух аргументов.
# """
#
# def my_func(a, b, c):
#     my_list = [a, b, c]
#     my_list.sort(reverse=True)
#     return sum(my_list[:2])
#
# print(my_func(23, 32, 42))
#
# """
# 4. Программа принимает действительное положительное число x и цклое отрицательное число y.
#     Выполнить возеление числа с в степень y.
#     Реализовать в виде функуии my_func(x,y).
#     Без встроенной функуии возведения числа в степень.
# """
#
# my_func_pow = lambda x, y: x**y
#
# def my_func(x: int, y: int) -> float: # вариант документации входных- выходных данных
#     if y > 0:
#         return
#     elif y == 0:
#         return 1
#     elif x <= 0:
#         return
#     else:
#         # return 1/x*my_func(x, y+1) # c помощью рекурсии
#         x_pow_y = 1
#         while y < 0:
#             x_pow_y *= 1/x
#             y +=1
#         return x_pow_y
#
# result = my_func_pow(2, -3)
# print(result)
# result = my_func(2, -3)
# print(result if result else "неверные входные данные")

# """
# 5. Запрагиваем у пользователя строку чисел, разделенных пробелом.
#     Выводится сумма чисел. Пользователь может продолжить ввод чисел,
#     разделенных пробелом. Сумма новых значений будет добовляться к уже подсчитанной сумме.
#     Если в место числв вводится символ, выполнение завершается.
#     Если символ введен помсле нескольких чисел, добавляем сумму этих чисел,
#     после завершить.
# """
# def sum_calc(input_string):
#     input_list = input_string.split()
#     my_sum = 0
#     for el in input_list:
#         if el:
#             try:
#                 if el == "N":
#                     return my_sum, False
#                 else:
#                     my_sum += float(el)
#             except ValueError:
#                 continue
#     return my_sum, True
#
# continue_flag = True
# result_sum = 0
# while continue_flag:
#     input_string = input("Введите числа без пробела. Для остановки введите N: ")
#     current_sum, continue_flag = sum_calc(input_string)
#     result_sum += current_sum
#     print("промежуточная сумма: ", result_sum)
# print("результирующая сумма: ", result_sum)

# """
# 6.Принимает слово из маленьких латинских букв и возвращающая его же
#     но с пропимной буквы. + Должна пападать строка из слов, разделеных пробелом
#     Каждое слово состоит из букв в нижнем регистре. Сдеоать вывод исзодной строки,
#     каждое слово начинатеся с заглавной буквы. Использовать ранее написанную int_func().
# """
#
# int_func = lambda word: word.title()
#
# input_string = input("введите строку: ")
# result_string_list = []
# input_words = input_string.split(" ")
# for el in input_words:
#     result_string_list.append(int_func(el))
#
# print(" ".join(result_string_list))
