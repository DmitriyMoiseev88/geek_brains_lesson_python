# #name = input('Имя: ')
# surname = input('Фамилия: ')
# age = int(input('Возраст: '))
# weight = int(input('Вес: '))

# if age <= 30 and weight >= 50 and weight <= 120:
# print(name, surname, age, 'год', 'вес', weight, '- у вас хорошее состояние')
# elif age > 30 and age <= 40 and (weight < 50 or weight > 120):
# print(name, surname, age, 'год', 'вес', weight, '- Нужно заняться собой')
# elif age > 40 and (weight < 50 or weight > 120):
# print(name, surname, age, 'год', 'вес', weight, '- Обратись к врачу!')

# hero = 'superman'
# if hero.find('man')  != -1:
# print('Есть')

# if 'man'in hero:
# print('Тоже есть')


# print('Сореввнование по Python')
# count = int(input('Введите колличество участников: '))
# i = count
# members = []
# while i >0:
# name = input('Кто занял {} место? '.format(i))
# members.append(name)
# i -= 1

# print('В соревноавниях участвовали: ',sorted(members))
# members.reverse()
# result = members[:3]
# result = 'Поздрваляем {} с победой! '.format(result)
# print(result)

# friends = ['Kate', 'Leo', 'Max']
# Цикл While
# i = 0
# while i < len(friends):
# friend = friends[i]
# print(friend)
# i += 1

# Цикл for
# for friend in friends:
# print(friend)
# print('end')

# Цикл Range
# numbers = range(66) #Выводится диапазон цисел, их не видим - тип данных range.
# print(numbers)
# print(list(numbers))

# numbers = [1, 3, 5] #Вывести не четные числа (если их 100 или 1000)
# for number in numbers:
# print(list(range(1, 100, 2)))

# for number in range(1, 100, 2):
# print(number)


# winners = ['Kate', 'Leo', 'Max']
# for i in range(1, len(winners) + 1):
# print(i, ')', winners[i-1])

# Работа со словарями (Dict)
# friend = {
# 'name' : 'Max',
# 'age' : 23
# }
# print(friend)
# print(type(friend))
# print(friend['age']) #Смотрим по ключу значение словаря

# friend['has_car'] = True #Добавление ключа и значения
# print(friend)
# friend['has_car'] = False #С одним,повторяющимся ключом - одно значение(иначе замена)
# print(friend)

# del friend['age'] #Удаление ключа со значением
# print(friend)

# if 'has_car' in friend: # Оператор in по ключам
# print('Есть машина')

# for key in friend.keys():
# print(key) #Перебор в цикле for по ключам
# print(friend[key]) # Для получения значения

# for key in friend:
# print(key) #Так же перебирает по ключам

# for val in friend.values():
# print(val) #Если не нужны ключи

# for item in friend.items(): #Перебор по картежем + можно использ. индекс
# print(item)

# for key, val in friend.items(): #Перебор по картежем, разбивая на 2 переменные
# print(key)
# print(val)

# Работв с множествами (не может быть одинаковых эллементов, тип set)
# cities = ['Vegas', 'Paris', 'Moscow', 'Paris', 'Vegas']
# print(set(cities)) # привел к типу set (не может быть одинаковых эллементов)

# cities = {'Vegas', 'Paris', 'Moscow'}
# cities.add('Burma') # Метод добавляет только не повторяющийся элем.
# cities.remove('Vegas') # Удаляем эллемент
# print(cities)

# max_things = {'Телефон', 'Бритва', 'Рубвшка', 'Шорты'}
# kate_thinnds = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# print(max_things | kate_thinnds) #Какие вещи взяли супруги вместк?  В выводе вещи не повторяются
# print(max_things & kate_thinnds) #Какие вещи повторяются?
# print('Какие вещи взялв Max но невзяла Kate: ', max_things - kate_thinnds) #Какие вещи взялв Max но невзяла Kate?
# print(kate_thinnds - max_things) #Какие вещи взялв Kate но невзяд Max?

# a =[1, 1, 1, 2, 2, 2, 3, 4]
# b = [2, 4, 5]
# for number in a[:]: #Удаляем через индекс, иначе будут повторы
# if number in b:
# a.remove(number)
# print(a)

# data = '02.11.2021'
# d, m, y = data.split('.')
# print(d, m, y)
# months = {
# '01' : 'января',
# '11' : 'ноября',
# }
# days = {
# '01' : 'первое',
# '02' : 'второе',
# }
# result = f' {days[d]} {months[m]} {y} года.'
# print(result)

# numbers = [1, 1, 2, 3, 3, 4, 4, 5, 1, 2, 7]
# result = []
# for number in numbers:
# if numbers.count(number) ==1:
# result.append(number)
# print(result)

# Создание игры "Угадай число"
# import random
# number = random.randint(1, 100)
# #print(number)
# user_number = None
# count = 0
# levels = {1:10, 2:5, 3:3}
# level = int(input('Выберете сложность:  '))
# max_count = levels[level]
# user_count = int(input('Введите колличество играков: '))
# users = []
# for i in range(user_count):
#     user_name = input(f'Введите имя игрока {i}: ')
#     users.append(user_name)
# print(users)
# is_winner = False
# winner_name = None
# while not is_winner:
#     count += 1
#     if count > max_count:
#         print('Все игроки проиграли')
#         break
#     print(f'Попытка № {count}')
#     for user in users:
#         print(f'Ход пользоаателя {user}')
#         user_number = int(input('Введите число: '))
#         if user_number == number:
#             is_winner = True
#             winner_name = user
#             break
#         elif number < user_number:
#             print('Ваше число больше загаданного')
#         else:
#             print('Ваше число меньше загаданого')
# else:
#     print(f'Победитель {winner_name}')

# import random
# min_number = 1
# max_number = 100
# result = None
# while result != '=':
#     comp_number = random.randint(min_number, max_number)
#     print(comp_number)
#     result = input('= > (загаданное число больше указанного) <')
#     if result == '=':
#         print('Победа')
#         break
#     if result == '>':
#         min_number = comp_number + 1
#     elif result == '<':
#         max_number = comp_number - 1
# else:
#     print('Победа')
# Функции
# numbers = []
# for i in range(3):
#     number = int(input('Введите число: '))
#     numbers.append(number)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# def get_sep(sep, sep_len):
#     return sep * sep_len
#
# print(get_sep( 'l', 50))
#
# sep = get_sep(')', 50)
# text = 'Hello {} Func {}'.format(sep, sep)
# print(text)


# Параметры функции
# def hello_dimon():
#     print('HELLO', 'DIMON')
#
# hello_dimon()
#
# def hello(who):
#     print('HELLO', who)
#
# hello('Dimon')
#
# def greeting(who, say):
#     print(say, who)
# greeting('Dimon', 'Privet')
# greeting('Anton', 'Bay')
#
# def greeting(who, say):
#     print(say, who)
# greeting('Dimon', 'Privet')
# greeting('Privet', 'Dimon')
# greeting(say = 'Privet', who = 'Dimon')
#
# def greeting(who, say = 'Hello'): # Параметр по умолчанию
#     print(say, who)
# greeting('Leo', 'Privet')
# greeting('Dimon')# пораметр по умолчанию
# greeting('Bil', 'Hi')# подствит свой параметр

# передача любого кол-ва параметров
# def greeting(say, *args): # * для передачи неограниченного кол - ва парамет.
#     #Называется аргс
#     print(say, args)
# greeting('Hello', 'max', 'Pol') # Параметров больше чем в функции
# greeting('hello', 'Dimon', 'ANNA', 'BIL') # Параметров больше чем в функции
#
#
# def get_person(**kwargs): # Аналогично примеру выше, параметры
#     for k, v, in kwargs.items():  # задаем по имени
#         print(k, v) # Возвращает словарь, с ним можно действовать
# get_person ( name = 'leo', age = 20, has_car = True, info = 'принимает любое количство параметров')

# ОБЛАСТЬ ВИДИМОСТИ ОБЬЕКТА
# def my_f (my_var):# передача переметорв в функцию
#     my_var = 999
#     print('Внутри функции:', my_var)
#
# a =1
# my_f(a) # Передал 1, вернула 999 ( внутренее значение)
# print('После выполнения функции', a)# Переменная с наружи не поменяла свое значение
#
# def some_f(): #Переменная без параметров
#     a = 999 # Не таже переменная, что и с наружи
#     print('переменная в нутри функции', a)
#
# a =  1
# some_f() # Другая область видимости и переменные
# print('переменная после выполнения функ:', a )
#

# M = 'Меня видно везде' # Глобальная для всех
# def a():
#     ma = 'Меня видно в b() и в a()' # глобальная для нижних
#
#     def b():
#         print(M)
#         print(ma)
#         mb = 'Меня видно в c() и в b() но не видно в a'
#
#         def c():
#             print(M)
#             print(ma)
#             print(mb)
#             mc = 'меня видно только в c'
#             print(mc)
#         c()
#     b()
# a()

# def my_filter(numbers, function): # Унивевсальные функции
#     result = []
#     for number in numbers:
#         if function(number):
#             result.append(number)
#     return result
#
# numbers = [ 1, 2, 3, 4, 5, 6, 7, 8]
# #def is_even(number):
#     #return number % 2 == 0
# print(my_filter(numbers,lambda number: number % 2 == 0))#Лямбда функции для создания анонимных фун.
# по месту использоваеия
# print(my_filter(numbers,lambda number: number % 2 != 0))#записыватся в одну стороку
# print(my_filter(numbers,lambda number: number > 4))

# cities = [('Москва', 1000), ('Лас-Вегас', 500), ('Атверпен', 2000)]
# print(sorted(cities))

# Функция MAP - применят функцию к каждому эллементу послкдоывтельности
# Не фильтрует, а получает новую
# nunbers = [ 5, 3, 4, 7, 8] # получить список квадратов
# print(list(map(lambda x: x**2, nunbers)))
# print(list(map(lambda x: str(x), nunbers))) # привести к строке

# РАЗБОР ДЗ;
# def by_count(city):
#     return city[1]
# print(sorted(cities, key = by_count))
# print(sorted(cities, key = lambda city: city[1]))

#
#
# МОДУЛИ И БИБЛИОТЕКИ: Встроенные. Сторониие (django.PyQt5). Свои(любой.py файл)
# здесь пример со встроенными млдудями : варианты подключения
# from math import* # Не рекомендуется, импорт всего содержимого модуля
# print(pi) # Когда импортируем все обьекты, не знаем с какими именами эти обьекты
# print(sin(30))
#
# from random import randint, randrange # Импорт конкретных функций библиотеки
# print(randint(1,10))

# Импорт конкретных функций библиотеки
# import math # подключение модуля целиком
# import random as rd # то же самое, как псевданим
# print(math.pi)
# print(math.sin(38)) # синус угла в радианах
# print(rd.randint(1,10))

# Использование модудя math
# import math
# r =  100
# print(2 * r * math.pi)# нахождение длинны окружности с определенным радиусом
#
# print((r ** 2) * math.pi)# нахождение полощади окружности с определенным радиусом
# print((math.pow(r, 2)) * math.pi) # то же нахождение полощади окружности с определенным радиусом (через функц. math)
#
# x1 = 10
# y1 = 10
# x2 = 50
# y2 = 100
# i = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)# по координатам 2-х точек найти расстояние между ними
# print(i)
#
# print(math.factorial(9))# Найти факториал числа 9


# Использование random(генерация случайных чисел, букв или последовательностей)
# from random import randint, choice, sample, shuffle
# print(randint(0, 100))# Загадать члучайное число от 0 до 100
#
# players = ['Max', 'Leo', 'Kate', 'Ron', 'Pol']
# print(choice(players))# Выбрать победителя из списка
# print(sample(players, 3))# Выбрать 3-x победелей из списка
#
# cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K']
# shuffle(cards)# перемешать карты
# print(cards)


# СОЗДАНИЯ СОБСТВЕННЫХ МОДУЛЕЙ
# модули - это файлы с расширением
#
# import os
# print(os.name) # Имя операционной сиитеиы
# print(os.getcwd) # Текушая рабочая дирректрия
# new_path = os.path.join(os.getcwd(), 'new_f')# Создаем ноаый пути
# os.mkdir(new_path)# Сосдаем папку по новому пути

# ФУНКЦИИ И ПЕРЕМЕННЫЕ SYS
# import sys
# print(sys.executable) # Путь до интерпритатора
# print(sys.platform)# Информация о платформе
# sys.exit()# Выход из python
# print('этот уже не выполнится')

# import sys
# print(sys.path)# Это список папок по которым python ищет модули
# print(type(sys.path))
#
# for p in sys.path: # для удобства в столбец
#     print(p)
#
# sys.path.append('D:') # Говорим python искать по этому пути
# import maymodul # Если создали на диске D

# import sys, os
# name = sys.platform
# for i in range(1, 6):
#     new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
#     os.mkdir(new_path)

# sys.argv(это переиенная командной сторокм при запуске скрипта python
# sys.argv[0] - путь до нашего серипта.
# python my_script.py part1 part 2part3... # Остальнве парпметры передаются при вызове скрипта через поробел

# ( w - запись, если нет, создаем новый. Если есть, перезапишется)
# ( x - запись, если нет, ошибка)
# ( a - дозапись)
# ( b - двоичный режим)
# ( + = открытие на чтоние и запись)
# РАБОТА С ФАЙЛАМИ. КОДИРОВКИ
# функция open и ее параметры
# - откоытие в указанном нами режиме
# f = open('first.txt', 'w')# (запись, файла не сущестует)
# f = open('first.txt', 'r')# чтение текста файла

# f = open('first.txt', 'w')
# f.write('Hello\n')# запись текста файла
# f.write('World\n')
#
# f.writelines(['HELLO\n', 'WORLD\n'])

# f = open('second.txt', 'r') #( r - чтение), файла не существует - будет ошибка
# f = open('first.txt', 'r')
# print(f.read())
# for line in f:
# print(line.replace('\n', ''))

# print(f.readlines())

# закрытие файла -  работа через with (менеджер контекста)
# f = open('first.txt', 'r')
# for line in f:
#    print(line.replace('\n', ''))
# f.close() # плох тем, что нужно помнить его

# with open('first.txt', 'r') as f: # не нужно помнить close
#     for line in f:
#       print(line.replace('\n', ''))
# print('end')
# Строки байт и кодировка
# s = 'Hello world'
# print(type(s)) # тип обычной строки

# sb = b'Hello bytes'
# print(type(sb)) # тип байтс
# print(s[1])
# print(sb[1])# взяьте индекса
# Любая информация хранится в виде 0 и 1
# ascii - америк. смиволы \ latin-1 - европейские символ. \ utf-8 - универсал код-ка для большинства язык.
# s = 'Hello bytes Мир'
# sb = s.encode('ascii')
# print(sb)
# print(type(sb))

# s = 'Hello bytes Мир'
# sb = s.encode('utf-8')
# print(sb)
# print(type(sb))
# print(s)
# print(type(s))
# # Декодирование. Обязательно тот же код, что и при encode
# s = sb.decode('utf-8')

# with open('bytes.txt', 'wb') as f:# Открыв.файл для записи байтов
#     f.write(b'Hello bytes')# Пишем строку байт
#
# with open('bytes.txt', 'r', encoding = 'ascii') as f: # Читаем как текст
#     print(f.read())
#
# with open('bytes.txt', 'wb') as f:
#     str = 'Привет мир'
#     f.write(str.encode('utf-8'))
#
# with open('bytes.txt', 'r', encoding = 'utf-8') as f:
#     print(f.read())

# ОТКРЫТИЕ ФАЙЛОВ ДЛЯ ЗАПИСИ БАЙТОВ
# with open('bytes.txt', 'wb') as f:
# with open('bytes.txt', 'w', encoding='utf-8') as f:
#     # str = 'Привет мир'
#     # f.write(str.encode('utf-8'))
#     f.write('Привет мир')
#
# with open('bytes.txt', 'rb') as f:
#      result = f.read() # читаем байты
#      print(result)
#      print(type(result))
#      s = result.decode('utf-8')
#      print(s)

# МОДУЛЬ ПИКЛЕ - универсальеный способ
# person = {'name': 'Max', 'phones': [ 123, 345]} # ручной способ записи
# # открываем файл
# with open('person.dat', 'wb') as f:
#     # запись построчно, с начало имя
#     name = person['name']
#     # записал с переносом строки и перевел в байты
#     f.write(f'{name}\n'.encode('utf-8'))
#     # из словаря получил телефоны
#     phones = person['phones']
#     # записал 1 телефон ы новую строку
#     for phone in phones:
#         f.write(f'{phone}\n'.encode('utf-8'))
#
# print('обьект записан')
#
# # загружаем файл
# with open('person.dat', 'rb') as f:
#     # нужно знать как записывали обьект
#     # прочитаем файл в список
#     result = f.readlines()
#
# # воссоздаем исходный обьект
# person = {}
# # первый эллемент это имя
# person['name'] = result [0].decode('utf-8').replace('\n', '')
# # далее телефоны
# phones = []
# for bphone in result[1:]:
#     phones.append(bphone.decode('utf-8').replace('\n', ''))
#
# person['phones'] = phones
# # получили исходный обьект - это долго и не просто
# print(person)

# CEРИАЛИЗАЦИЯ, МОДУЛЬ ПИКЛЕ - универсальеный способ
# import pickle
# person = {'name': 'Max', 'phones': [ 123, 345], 'age': 20}
# # # открываем файл
# with open('person.dat', 'wb') as f:
#     # сразу пишем обьект целиком
#     pickle.dump(person, f)
# print('обьект записан')
#
# with open('person.dat', 'rb') as f:
#     person = pickle.load(f)
#
# print(person)#

# МОДУЛЬ json
# print(type(friends))
# # # преобразуем список в json
# # json_friends = json.dumps( friends)
# # print(json_friends)
# # print(type(json_friends))
# #
# # # Обратно из json в обьект
# # friends = json.loads(json_friends)
# # print(friends)
# # print(type(friends))
# with open('friends.jon', 'w') as f:
#      # переобразуем список друзей в json и сохраняем файл
#      json_friends = json.dump(friends, f)
# # обратно из файла в обьект
# with open('friends.jon', 'r') as f:
#      friends = json.load(f)
#
# print(friends)
# print(type(friends))

# РЕШЕНИЕ ЗАДАЧИ : Передать список любимых песен и исполнителей, разработчику C#
# import json
# # с начала сохраняем в удобный формат(json)
# favorite_tracks = [
#      {'name': 'Вечная любовь', 'artist': 'Агата Кристи'},
#      {'name': 'Angel', 'artist': 'Massive Attck'},
#      {'name': 'Jamping', 'artist': 'Bod Marley'}
# ]
# with open('tracks_json', 'w', encoding = ('utf-8')) as f:
#      json.dump(favorite_tracks, f)
#
# Обработка исключений
# тернальный оператор
# в общем виде: результат 1 если условие иначу результат 2
# is_his_name = False
# name = 'Max' if is_his_name else 'Empty'
# print(name)
#
# is_one = True
# number = 1 if is_one else 2
# print(number)
#
# is_russian = True
# print('Привет' if is_russian else 'Hello')


# word = 'привет'
# result = [] # простой вариант
# for i in range(len(word)):
#     if i%2 !=0:
#         letter = word[i].lower()
#     else:
#         letter = word[i].upper()
#     result.append(letter)
#
# result = ''.join(result)
# print(result)

# for i in range(len(word)):
#     letter = word[i]
#     letter = letter.lower() if i%2 !=0 else letter.upper()
#     result.append(letter)
#
# result = ''.join(result)
# print(result)

# password = input('Введите пароль')
# print('ВХОДИ' if password == 'secret' else 'ЗАКРЫТО')
# ГЕНЕРАТОРЫ списка и словарей
# синтаксическая констр позволяюшая по определенным правилам
# создавать заполненые списки
# numbers = [1, 2, 3, 4, 5, -1, -3, -3, -4]
# # Классический способ
# result = []
# for i in numbers:
#     if i > 0:
#         result.append(i)
# print(result)
# Через функцию фильтер
# result = filter(lambda number: number > 0, numbers)
# print(list(result))
# Через генератор
# result = [number for number in numbers if number > 0 ]
# print(result)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
# # классический способ
# result = {}
# for pair in pairs:
#     key = pair[0]
#     val = pair[1]
#     result[key] = val
#
# print(result)
# # Через генератор словаря
# result = {pair[0]: pair[1] for pair in pairs}
# print(result)
#
# import random
# # Создание списка случайных чисел от 1 до 100
# numbers = [random.randint(1, 100) for i in range(1, 10)]
# print(numbers)
# # Создать список квадратных чисел
# numbers = [1, 2, 3, -4]
# numbers = [number ** 2 for number in numbers]
# print(numbers)
# # Список имен на букву А
# names = ['Руслан', 'Димсон', 'Алексей', 'Андрей']
# names = [name for name in names if name.startswith('А')]
# print(names)

# import math
# numbers = [1, 2, 3, 4, 5, -1, -3, -3, -4]
# # Классический способ
# result = []
# for i in numbers:
#     if i > 0:
#         sqrt = math.sqrt(i)
#         if sqrt < 2:
#             result.append(i)
# print(result)
#
# result = []
# for i in numbers:
#     if i > 0 and math.sqrt(i) < 2:
#         result.append(i)
# print(result)
#
# result = [i for i in numbers if i > 0 and math.sqrt(i) < 2]
# print(result)

# def add_input_list(input_list = None):
#     if input_list is None:
#         input_list = []
#     input_list.append(2)
#     return (input_list)
#
# result = add_input_list()
# print(result)
# result = add_input_list([0, 1])
# print(result)

# Тоже через or
# def add_input_list(input_list = None):
#     # Используем свойства or вместо условия
#     input_list = input_list or []
#     input_list.append(2)
#     return (input_list)
#
# result = add_input_list()
# print(result)
# result = add_input_list([0, 1])
# print(result)

# МОДУЛЬ COPY
# a = 1
# b = a
# b = 100
# print(a)
# # Со списком будет изменение
# a = [1, 2, 3]
# b = a
# b[1] = 100
# print(a)
#
# numbers = [1, 2, 3]
# def change_number_in_list(input_list):
#     input_list[1] = 200
# # После вызова функции
# change_number_in_list(numbers)
# # список в основной прог. изменится
# print(numbers)

# Копируем список, что бы не меняляся
# import copy
# a = [1, 2, [1, 2]]
# b = copy.deepcopy(a)
# b[2][0] = 200
# print(a)
# print(b)
# ИСКЛЮЧИТЕЛЬНЫЕ СИТУАЦИ
# number = int(input('Введите число'))
# try:
#     #код который может вызывать исключительную ситуацию
#     result = 100 / number
# except ZeroDivisionError as e:
#     # что делать если возникла исключительная ситувция
#     print('Попытка деления на ноль')
#     print('Информация об исключении', e)
# except Exception as e:
#     print('Неизвестная ошибка')
#     print('Информация об исключении', e)
# else:
#     # что делать если ошибок нет
#     print('Все хорошо ошибок не было')
# finally:
#     # выполняется всегда
#     print('что делаем кода ошибка есть и когда нет')
# Когда нужно создать исключительную ситуацию
# print('Начало')
# raise Exception ('Что то пошло не так')
# print('Конец')

# ДЗ: Даны два списка - получить список присут-ий в обоих исход.
# fruits_2 = ['banana', 'kiwi', 'tangerine']
# fruits_1 = ['apple', 'banana', 'orange', 'kiwi', 'rear']
# result = []
# for fruit in fruits_1:
#     if fruit in fruits_2:
#         result.append(fruit)
# print(result)
#
# result= [fruit for fruit in fruits_1 if fruit in fruits_2]
# print(result)

# numbers = [1, 5, -9, 10, 27, 8, 17, 45, 100, 11, -7, 12, -27]
# result = [number for number in numbers if number > 0 and number % 3 == 0 and number % 4 != 0]
# print(result)

# функция принимает на вход список
# создает из списка - список квадратных корней
# возвращает результат
# import math
# old_list = [1,-1, 2,-2, 4, 5, 6, 7, 8, 9]
#
# def new_sqrt_list (input_list):
#     result = [math.sqrt(number) if number > 0 else number for number in input_list]
#     return result
#
# # плохой пример из -за индексов + цикл не даст удалить элемент
# #    input_list = input_list.copy()
# #     for i in range(len(input_list)):
# #         number = input_list[i]
# #         if number > 0:
# #             input_list[i] = math.sqrt(number)
# #     return input_list
#
# result = new_sqrt_list(old_list)
# print(result)
# print(old_list)
#
# def unlucky_number(number):
#     if number == 13:
#         raise ValueError('Несчастливое число')
#     else:
#         return number ** 2
#
# number = int(input('Введите число'))
#
# try:
#     result = unlucky_number(number)
# except ValueError:
#     print('У нас не счатливое число')
# else:
#     print(result)

# ПРАКТИКУМ. Консольно файловый менеджер
# функция для создания файла
# import os
# import shutil
# import datetime
#
#
#
# def create_faile(name, text=None):
#     with open(name, 'w', encoding='utf-8') as f:
#         if text:
#             f.write(text)
#
#
# def create_folder(name):
#     try:
#         os.mkdir(name)
#     except FileExistsError:
#         print('Такая папка уже есть')
#
#
# def get_list(folders_only=False):
#     result = os.listdir()
#     if folders_only:
#         result = [f for f in result if os.path.isdir(f)]
#     print(os.listdir())
#
# def delete_file(name):
#     if os.path.isdir(name):
#         os.rmdir(name)
#     else:
#         os.remove(name)
#
# def copy_file(name, new_name):
#     if os.path.isdir(name):
#         try:
#             shutil.copytree(name,new_name)
#         except FileExistsError:
#             print('Такая папка уже есть')
#     else:
#         shutil.copy(name, new_name)
#
# def save_info(messege):
#     current_time = datetime.datetime.now()
#     result = f'{current_time} - {messege}'
#     with open('log.txt', 'a', encoding='utf-8') as f:
#         f.write(result + '\n')
#
# if __name__ == '__main__':
#     create_faile('text.dat')
#     create_faile('text.dat', 'some text')
#     create_folder('new_f')
#     get_list(True)
#     # delete_file('new_f')
#     # delete_file('text.dat')
#     copy_file('new_f', 'new_2')
#     copy_file('text.dat', 'text.dat_2')
#     save_info('abc'