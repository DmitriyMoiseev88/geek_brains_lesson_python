# temperature = -25
# weather = 'солнечно'
# print('Сегодня',  weather)
# print('Температура воздуха ', str(temperature), 'градусов')
#
# speed_kmh = 1079252848.
# sek_in_hour = 60 * 60
# speed_kms = speed_kmh / sek_in_hour
# print('Скорость света равна', int(speed_kms), 'км/с')
#
# #Дробные числа приводят к целым функцией int()
# # Обратите внимание: int() не округляет числа по правилам арифметики,
# # а просто отбрасывает дробную часть.
# snake = ('38.2')
# length = 6.5
# result = float(snake) * length
# print('В вагоне можно поставить в ряд', int(result), 'попугаев')
#
# #Можно сделать несколько преобразований в одной строке:
# # сначала превратить дробь в целое число,
# # а затем преобразовать в строку:
# #fraction = 1.5  # Дробь
# #print("Целая часть = " + str(int(fraction)))
# # Вернётся строка, представляющая собой целочисленную часть дроби.
#
# #СПИСКИ
# #Списки — это последовательности чисел, строк или каких-то ещё значений.
# #Содержимое списка пишется в квадратных скобках,
# # элементы списка разделяются запятой:
# print("Привет, я Анфиса!")
# friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']
#
# #У каждого элемента есть свой порядковый номер — индекс.
# # С помощью индекса можно получить значение элемента списка.
# friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']
# index = 3
# #print(friends[3])
# print('Привет, ' + friends[index] + ', я Анфиса!')
#
# print("Привет, я Анфиса!")
# friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']
# index = 4
# print(friends[index], ' живёт в Красноярскe')
#
# #Для подсчёта элементов списка есть стандартная функция len().
# # 1) Объявите переменную count и сохраните в ней количество друзей.
# # Посчитайте их вызовом функции len().
# print("Привет, я Анфиса!")
# friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']
# count = len(friends)
# print('У тебя', count, 'друзей')

#Объединение строк
# bayan = ['[', ':', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', ':', ']']
#  превращаем список в баян методом join()
# print(' '.join(bayan))
#метод join
# впервые используем такой инструмент, как метод.
# Это разновидность функции.
# Тоже мини-программа из Python, тоже аргументы в круглых скобках.
# метод в коде привязывается к объекту, в нашем случае — к строке.
#Вызов метода записывают всегда так:
#объект.имя_метода(аргументы_метода)

# pushkin = ['божество', 'вдохновенье', 'жизнь', 'слёзы', 'любовь']
# text = ', и '.join(pushkin)
# print('Что было после чудного мгновенья: и ' + text)
#
# print("Привет, я Анфиса!")
# friends = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']
# friends_string = ', '.join(friends)
# print('Твои друзья: ' + friends_string)
#
# stations = ['Москва', 'Серп и Молот', 'Карачарово', 'Чухлинка', 'Кусково',
#             'Новогиреево', 'Реутово', 'Никольское', 'Салтыковская', 'Кучино',
#             'Железнодорожная', 'Чёрное', 'Купавна', '33-й километр', 'Электроугли',
#             '43-й километр', 'Храпуново', 'Есино', 'Фрязево', '61-й километр',
#             '65-й километр', 'Павлово-Посад', 'Назарьево', 'Дрезна', '85-й километр',
#             'Орехово-Зуево', 'Крутое', 'Воиново', 'Усад', '105-й километр', 'Покров',
#             '113-й километр', 'Омутище', 'Леоново', 'Петушки']
# print(' - '.join(stations))

#Урок 2. Циклы
# повторяет определённый набор действий
# до тех пор, пока выполняется какое-то заданное условие.

# Урок 3. Диапазоны от и до
#функция range(). В неё передаются два целых числа:
# начало и конец диапазона. В результате будет создана последовательность,
# включающая все целые числа в указанном диапазоне.
#Особенность этой последовательности в том,
# что в неё не включается последнее число диапазона:
#Числа могут быть и отрицательными,
# важно, чтобы первое число было меньше второго.
#around_zero = range(-3, 3)
# Последовательность around_zero будет включать в себя числа -3, -2, -1, 0, 1 и 2.
#for i in range(-3, 3):
    #print(i)
#Задать диапазон можно прямо в условии цикла, без промежуточной переменной around_zero.
# Цикл переберёт все числа в диапазоне от -3 до 3 и напечатает их:
#print('Это первый этаж.')
# for i in range(2, 11):
#     # Здесь вместо многоточий
#     # вставьте номер текущего этажа,
#     # вычислите и вставьте номер предыдущего этажа.
#     print('А это', i, 'этаж, он на один выше, чем этаж', i -1)

#Если нужно пройтись по списку или по диапазону чисел в обратном порядке
# вызывайте функцию reversed(): она переворачивает и список, и диапазон;
# чтение любой последовательности начнётся с конца.

# countdown_str = ''
# for i in reversed(range(0, 11)):
#     countdown_str = countdown_str + str(i) + ', '
#
# countdown_str = countdown_str + 'поехали!'
# print(countdown_str)
# Урок 5. Ветвления
# for messages_count in range(6):
#     if messages_count > 0:
#         print('Новых сообщений:', messages_count)
#     else:# Дописан блок во 2 задании
#         print('У вас нет сообщений')
#
# for current_hour in range(24):
#     if current_hour < 12:
#         print('Доброе утро! Димася')
#     else:
#         print('Добрый день! Димон')

#Урок 7. Множественные ветвления
# for messages_count in range(0, 21):
#     if messages_count == 0:
#         print('У вас нет новых сообщений')
#     elif messages_count == 1:
#         print('У вас 1 новое сообщение')
#     elif messages_count <= 4:
#         print('У вас', messages_count, 'новых сообщения')
#     else:
#         print('У вас',  messages_count, 'новых сообщений')
#
# for current_hour in range(0, 24):
#     print("На часах " + str(current_hour) + ":00.")
#     if current_hour <= 5:
#         print('Доброй ночи!')
#     elif current_hour <= 11:
#         print('Доброе утро!')
#     elif current_hour <= 17:
#         print('Добрый день!')
#     elif current_hour <= 22:
#         print('Добрый вечер!')
#     else:
#         print('Доброй ночи!')

#Урок 9. Логические выражения
# for current_hour in range(0, 24):
#     print("На часах " + str(current_hour) + ":00.")
#
#     if current_hour >= 6 and current_hour <= 11:
#         print('Доброе утро!')
#     elif current_hour >= 12 and current_hour <= 17:
#          print('Добрый день!')
#     elif current_hour >= 18 and current_hour <= 22:
#         print('Добрый вечер!')
#     elif current_hour <= 5 or current_hour >= 23:
#          print('Доброй ночи!')


# for messages_count in range(0, 100):
#     remainder = messages_count % 10
#     if messages_count == 0:
#         print('У вас нет новых сообщений')
#     elif remainder == 0 or remainder >= 5 or (messages_count >= 11 and messages_count <= 19):
#         print('У вас', messages_count, 'новых сообщений')
#
#
#     elif remainder == 1:
#         print('У вас', messages_count, 'новое сообщение')
#
#     else:
#         print('У вас', messages_count, 'новых сообщения')
#
# # Урок 11. Составные логические выражения
# good_boy = True  # мальчик-то неплохой
#
# if not good_boy:
#     print('Этот в грязь полез')
#     print('и рад,')
#     print('что грязна рубаха.')
#     print('Про такого говорят:')
#     print('он плохой, неряха.')
# else:
#     print('Этот чистит валенки,')
#     print('моет сам галоши.')
#     print('Он хотя и маленький,')
#     print('но вполне хороший.')
#
# # Урок 2. Функции
# def print_friends_count(friends_count):
#     remainder = friends_count % 10
#     if friends_count == 0:
#         print('У тебя нет друзей')
#     elif remainder == 0 or remainder >= 5 or (10 <= friends_count <= 19):
#         print('У тебя', friends_count, 'друзей')
#     elif remainder == 1:
#         print('У тебя', friends_count, 'друг')
#     else:
#         print('У тебя', friends_count, 'друга')
#
#
# print_friends_count(10)
# print_friends_count(3)
# print_friends_count(1000500)
#
# #Аргумент функции — это переменная, которая используется внутри функции.
# # Значение этой переменной присваивается при вызове функции.
#
# def print_friends_count(friends_count):
#     remainder = friends_count % 10
#     if friends_count == 0:
#         print('У тебя нет друзей')
#     elif remainder == 0 or remainder >= 5 or (10 <= friends_count <= 19):
#         print('У тебя', friends_count, 'друзей')
#     elif remainder == 1:
#         print('У тебя', friends_count, 'друг')
#     else:
#         print('У тебя', friends_count, 'друга')
#
# for friends_count in range(1, 11):
#     print_friends_count(friends_count)

# Урок 3. Аргументы функции
#В Python аргументам функций может быть присвоено «значение по умолчанию».
# Оно будет применено, если при вызове функции вы не передали ожидаемый аргумент.
#При вызове функции можно явно указывать, какому аргументу какое значение соответствует.
# В таком случае порядок следования аргументов в скобках роли не играет.
# def print_friends_count(friends_count, name= ''):
#     if friends_count == 1:
#         text = '1 друг'
#     elif 2 <= friends_count <= 4:
#         text = str(friends_count) + ' друга'
#     elif friends_count >= 5:
#         text = str(friends_count) + ' друзей'
#     if name == '':
#         text = 'У тебя ' + text
#         print(text)
#     else:
#         text = name + ', у тебя ' + text
#         print(text)
#
#
# print_friends_count(3, 'Артём')
# print_friends_count(friends_count=7, name='Марина')
# print_friends_count(6)
# print_friends_count(4, name='Настя')
#
# Урок 5. Разбиение на функции
# В больших проектах, написанных на Python,
# принято выносить весь повторяющийся код
# в отдельные функции перед телом основной программы.
#
# код функции say_hello
# def say_hello(current_hour):
#     if current_hour <= 5 or current_hour >= 23:
#         print('Доброй ночи!')
#     elif current_hour >= 6 and current_hour <= 11:
#         print('Доброе утро!')
#     elif current_hour >= 12 and current_hour <= 17:
#         print('Добрый день!')
#     elif current_hour >= 18 and current_hour <= 22:
#         print('Добрый вечер!')
#
#
# # перенесли основной код внутрь функции runner()
# def runner():
#     say_hello(4)
#     say_hello(10)
#     say_hello(15)
#     say_hello(20)
#
#
# # в теле программы остаётся только один вызов:
# runner()
# Функция say_hello() содержит основную логику,
# а runner() выполняет роль управляющего механизма.
#
#
# Подготовка кода к использованию на сервере.
#
# Урок 6. Счётчики

# comfort_count(may_2017)
# comfort_count(may_2018)

# Урок 7. Возврат значений из функции
# обычно задача функции не сводится к выступлениям в печати.
# Как правило, это код, производящий специальные вычисления.
# Он возвращает результат как значения  в вызывающий код, и там будет использовано.
# Например, сохранено в переменной.
# def calc_perimeter(side_a, side_b):
#     return (side_a + side_b) * 2
#
# may_2018 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23, 18, 22, 23, 11]
# may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]
#
# def comfort_count(temperatures):
#     count = 0
#     for temp in temperatures:
#         if 22 <= temp <= 26:
#             count += 1
#     return count
#
# print(comfort_count(may_2017))
#
# # функция для вычисления площади прямоугольника
# def calc_square(side_a, side_b):
#     return side_a * side_b
#
# a = 8
# b = 10
# p = calc_perimeter(a, b)
# s = calc_square(a, b)
# print('Периметр прямоугольника равен ' + str(p) + ' м.')
# print('Площадь прямоугольника равна ' + str(s) + ' кв. м.')
# Возвращённое значение не обязательно сохранять в переменной.
# Можно сразу вывести на экран:
# print('Площадь прямоугольника равна ' + str(calc_square(3, 4)) + ' кв. м.')

# FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']
#
# def show_count_friends(count_friends):
#     if count_friends == 1:
#         return 'У тебя 1 друг'
#     elif 2 <= count_friends <= 4:
#         return 'У тебя ' + str(count_friends) + ' друга'
#     elif count_friends >= 5:
#         return 'У тебя ' + str(count_friends) + ' друзей'
#
#
# def process_query(query):
#     if query == 'Сколько у меня друзей?':
#         count = len(FRIENDS)
#         return show_count_friends(count)
#     elif query == 'Кто все мои друзья?':
#         friends_string = ', '.join(FRIENDS)
#         return 'Твои друзья: ' + friends_string
#     else:
#         return '<неизвестный запрос>'
#
# print(process_query('Сколько у меня друзей?'))
# print(process_query('Кто все мои друзья?'))
# print(process_query('Как меня зовут?'))

# Словари и множества/Урок 1. Словари
#Словарь оформляется фигурными скобками. Его заполняют пары, записанные через запятую.
# Первый элемент в паре называется ключ, а второй — значение, они разделяются между собой двоеточием.

# friends = {'Серёга': 'Омск', 'Соня': 'Москва', 'Дима': 'Челябинск'}
# #print(friends['Серёга'])
#
# friends['Серёга'] = 'Магнитогорск'
# print('Серёга теперь живёт в славном городе ' + friends['Серёга'])
#
# #Ключи в словаре похожи на индексы списков.
# #Только индексами выступают натуральные числа,
# # а ключами бывают и числа обоих типов, и строки, и даже булевы значения True и False:
#
# #Чтобы такие списки использовать в коде,
# # их обычно превращают в строки методом join():
# patronymic = {'Илья': 'Ильич', 'Иван': 'Ивановна', 'Пётр': 'Петровна'}
# print(", ".join(patronymic.values()))
#
# Урок 2. Расширение словаря
#Расширяя словарь, имейте в виду, что из нескольких пар с одинаковыми ключами
# Python видит только одну — ту, что записана или добавлена последней:
# friends =  {'Серёга': 'Омск', 'Соня': 'Москва', 'Дима': 'Челябинск'}
# friends['Димон'] = 'СПБ'
# #print(friends)
# print("Вот в каких городах живут мои друзья:" ' ' + ', '.join(friends.values()))
#for friend, city in friends.items(): # Перебор элементов словаря
    #print(friend + ' живёт в городе ' + city)
#Урок 4. Перебор элементов словаря
#Пройти по всем элементам словаря можно циклом for,
# причём есть несколько вариантов:
#  favorite_songs = {
#     'Тополиный пух': 'Иванушки international',
#     'Город золотой': 'Аквариум',
#     'Звезда по имени Солнце': 'Кино'
# }
#
# for track in favorite_songs:
#     print(track + ' это песня группы ' + favorite_songs[track])
# #Этот способ позволяет пробежать по всем ключам словаря.
# track здесь — просто название переменной, оно могло быть любым

#Ещё можно пройти отдельно по значениям словаря:
# for music_band in favorite_songs.values():
#     print('Доктор, я больше не могу слушать группу ' + music_band)
#
# # И по ключам и значениям одновременно:
# for track, music_band in favorite_songs.items():
#     print(track + ' это песня группы ' + music_band)
# метод items() - но возвращает набор пар ключ-значение, поэтому при переборе
# мы используем две переменных — track и music_ban

# favorite_songs = {
#     'Серёга': ["Unforgiven", "Holiday", "Highway to hell"],
#     'Соня': ["Shake it out", "Don't stop me now", "Наше лето"],
#     'Дима': ["Владимирский централ", "Мурка", "Третье сентября"]
# }
# print(len(favorite_songs['Дима']))# Длина значений по ключу
# print( ', '.join(favorite_songs['Соня']))# напечатаетвсе любимые песни Сони через запятую и пробел ', '.join()

# friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
# friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']
# friends = {}
# # создать новую пару ключ-значение: имя_словаря[ключ] = значение
# for i in range(0, len(friends_names)):# В теле цикла соберём словарь, ссылаясь на список с именами друзей в качестве ключей
#     # и список с городами в качестве значений:
#     friends[friends_names[i]] = friends_cities[i]
#
# print(friends)
# print("Лена живёт в городе " + friends['Лена'])

# Урок 5. Множества
# в случае, если у нескольких песен один и тот же исполнитель, он появляется в выводе несколько раз.
#  Вот когда нам поможет новый тип данных set. Множества
# Тип set очень похож на список,
# 1) Элементы в сете не повторяются, автоматически не вписывая их
# 2) Не гарантируется, что при выводе элементов на экран будет соблюден какой-то определенный порядок.
# Любой список можно превратить в сет простым вызовом функции set()
# bands = ['Пикник', 'Ария', 'Блестящие', 'Блестящие']
# unique_band_names = set(bands)
# # По элементам сета тоже можно пройти циклом
# for band in unique_band_names:
#     print('Доктор, я не могу больше слушать группу ' + band)

# cities = ['Вологда', 'Чебоксары', 'Тольятти', 'Вологда'] # Список
# unique_cities = set(cities) # преобразовал во множества - сет
# print(', '.join(unique_cities)) # join() работает и для множеств тоже!

# cities = ['Санкт-Петербург', 'Хабаровск', 'Казань', 'Санкт-Петербург', 'Казань']
# unique_cities_group = set(cities)
# for city in unique_cities_group:
    #print('У меня есть друг в городе '+ city)

# Урок 7. Проверка наличия элемента
# В Python списки, словари и множества называются коллекции.
# Их можно легко различить по записи:
# sleep_list = ['спать', 'дрыхнуть', 'кемарить', 'почивать', 'спать']  # список
# sleep_dict = {'спать': 'дрыхнуть', 'почивать': 'кемарить'}  # словарь
# sleep_set = {'дрыхнуть', 'спать', 'почивать', 'кемарить'}  # множество; фигурные скобки в этом случае то же, что вызов set()
# Проверить, есть ли определённый элемент в списке или множестве, можно условной конструкцией оператором in
# ssleep_dict = {'спать': 'дрыхнуть', 'почивать': 'кемарить'}  # словарь
# if 'дрыхнуть' in sleep_dict:
#     print('есть такое!')
# else:
#     print('а что это?')
# Особенность есть у словарей — в них in засекает только ключи:
# список животных в лесу Белого Рыцаря
# forest_list = ['лось', 'коза', 'барсук', 'глухарь', 'лиса', 'ёж', 'пчела', 'синица', 'заяц']
# if 'слонёнок' not in forest_list:
#     print('но нету слонёнка в лесу у меня,')
#     print('слонёнка весёлого нет!')
# # список животных в лесу Белого Рыцаря
# forest_list = ['лось', 'коза', 'барсук', 'глухарь', 'лиса', 'ёж', 'пчела', 'синица', 'заяц']
# Когда нужно написать условие, что чего-нибудь в коллекции нет, помогает логический оператор not
# У списков есть метод append(), который добавляет свой аргумент в конец списка:
# Можно написать функцию пополнения любых списков, назовём её new_one
# def new_one(some_list, new):
#     if new in some_list:
#         print('такое у нас уже есть')
#     else:
#         print('а это что-то новое, берём')
#         some_list.append(new)
#     print(some_list)
#
# sleep_list = ['спать', 'дрыхнуть', 'кемарить', 'почивать', 'спать']
# new_one(sleep_list, 'баиньки')

# def is_anyone_in(collection, city):
#     if city in collection.values():  # если есть среди значений словаря collection
#         for name in collection: # переберите все ключи словаря
#             if collection[name] == city:  # если соответствующее ключу значение равно city
#                 print('В городе ' + city + ' живёт ' + name + '.')
#     else:
#         print('Пока никого.')
#
# friends = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Хабаровск',
#     'Егор': 'Пермь'
# }
# is_anyone_in(friends, 'Хабаровск')

# Урок 8. Операции с множествами
# Если вы хотите добавить в множество новый элемент,
# примените к сету метод add().
# Множества в Python хороши тем, что их легко объединять.
# Для объединения двух множеств к первому применяют метод union(), передавая ему второе множество как аргумент:
#songs1 = {'Три белых коня', 'Happy new year', 'Снежинка'}
#songs2 = {'Last christmas', 'Снежинка', 'Happy new year'}
#print(songs1.union(songs2))

#метод difference(). Его вызов записывается как
# set1.difference(set2) и возвращает новое множество, которое содержит только те элементы,
# которые присутствуют в set1, но отcутствуют в set2.
# my_songs = {'Наше лето', 'Голубой вагон', 'Облака'}
# friends_songs = {'Голубой вагон', 'Облака', 'Yesterday', 'Наше лето'}
#
# print(friends_songs.difference(my_songs))

# intersection(): пересечение двух множеств, то есть элементы, которые есть в обоих.
# my_films = {'Форсаж', 'Достучаться до небес', 'Мстители: война бесконечности'}
# friends_films = {'Мстители: война бесконечности', 'Форсаж', 'Матрица'}
#
# print(my_films.intersection(friends_films))
# def print_shopping_list(recipe1, recipe2):
#     #unique_recipe = recipe1 + recipe2
#     #unique_recipe1 = set(unique_recipe)
#     shopping_list = set(recipe1).union(set(recipe2))
#     print(', '.join(shopping_list))

# def print_shopping_list(dish1, dish2):
#     ingredients = set(dish1.keys()).union(set(dish2.keys()))
#     for i in ingredients:
#         amount = 0
#         if i in dish1:
#             amount += dish1[i]
#         if i in dish2:
#             amount += dish2[i]
#         print(i + ':', amount)

# pizza = {'мука, кг': 1,
#          'помидоры, кг': 1.5,
#          'шампиньоны, кг': 1.5,
#          'сыр, кг': 0.8,
#          'оливковое масло, л': 0.1,
#          'дрожжи, г': 50}
# salad = {'огурцы, кг': 1,
#          'перцы, кг': 1,
#          'помидоры, кг': 1.5,
#          'оливковое масло, л': 0.1,
#          'листья салата, кг': 0.4}
#
# print_shopping_list(pizza, salad)

# Урок 9. Прототип запроса к базе данных

# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }
#
#
# def format_friends(friends_count):
#     if friends_count == 1:
#         return 'У тебя 1 друг'
#     elif 2 <= friends_count <= 4:
#         return 'У тебя ' + str(friends_count) + ' друга'
#     elif friends_count >= 5:
#         return 'У тебя ' + str(friends_count) + ' друзей'
#
#
# def process_query(query):
#     if query == 'Сколько у меня друзей?':
#         count = len(DATABASE)
#         return format_friends(count)
#     elif query == 'Где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         string_cties = ', '.join(unique_cities)
#         return 'Твои друзья в городах: ' + string_cties
#     elif query == 'Кто все мои друзья?':
#         friends_string = ', '.join(DATABASE)
#         return 'Твои друзья: ' + friends_string
#     else:
#         return '<неизвестный запрос>'
#
#
# def runner():
#     print('Привет, я Анфиса!')
#     print(process_query('Сколько у меня друзей?'))
#     print(process_query('Кто все мои друзья?'))
#     print(process_query('Где все мои друзья?')) # добавил новый запрос
#
#
# runner()
#
# Разбить фразу на слова, и вообще разделить строку по определённому символу
# методом split(). В результате получится список строк.Метод принимает аргумент, указывающий,
# какой разделитель использовать.
# blok_string = 'Ночь. Улица. Фонарь. Аптека'
# # # из строки получаем список, где строку делят по сочетанию точки и пробела:
# Если в вызове split() не указывать разделитель, то строка разобьётся по пробелам:
# blok_list = blok_string.split('. ')
# print(blok_list)
# # print(type(blok_string))
# # можно получить, к примеру, последнее слово:
# print(blok_list[-1])
# print(blok_list[3])
# Лишние символы удобнее всего убирать методом strip()
# он убирает указанные символы в начале и в конце.

# def check_query(query):
#     tokens = query.split(',')
#     qustion = tokens[1]
#     return qustion.strip()
#
#
# queries = [
#     'Анфиса, сколько у меня друзей?',
#     'Андрей, ну где ты был?',
#     'Андрей, ну обними меня скорей!',
#     'Анфиса, кто все мои друзья?'
# ]
#
# for q in queries:
#     result = check_query(q)
#     print(q, '-', result)

# Урок 3. Форматирование строк
# f-строки включают имена переменных внутри фигурных скобок.
# Значения переменных подставляются в строку автоматически.
# one_hundred = 100
# rubles = 'рублей'
# friends = 'друзей'
# print(f'Не имей {one_hundred} {rubles}, а имей {one_hundred} {friends}.')

#      Урок 4. Подробнее форматировании
# f-строки можно подставлять не только переменные,
# но и результаты вычислений. Например, арифметические операции:
# one_hundred = 100
# five_hundred = 500
# print(f'{one_hundred} + {five_hundred} = {one_hundred + five_hundred}')
#
# one_hundred = 'сто'
# five_hundred = 'пятьсот'
# print(f'{one_hundred} + {five_hundred} = {one_hundred + five_hundred}')
#
# # И обращение к элементам списка:
# russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
#                     'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#
# print(f'«{russian_alphabet[-1]}» - последняя буква в алфавите.')

# к элементам словаря по ключу:
# favorite_songs = {
#     'Тополиный пух': 'Иванушки international',
#     'Город золотой': 'Аквариум',
#     'Звезда по имени Солнце': 'Кино'
# }
# song = 'Город золотой'
# print(f'«{song}» - одна из известных пеcен группы «{favorite_songs[song]}».')

#не злоупотребляйте этой возможностью (вставлять очень сложные выражения внутрь f-)
# Иначе получится перегруженный код, в котором будет сложно разобраться.
# Лучше придерживаться общего правила: f-строки используются только для форматирования вывода
# а вычислять все выражения надо вне их. И вообще, не стоит экономить на количестве строчек кода
# принося в жертву его читаемость.
# def calc_stat(listened):
#     N = len(listened)
#     return f'Вы прослушали {N} песен.'
#
# print(calc_stat([193, 148, 210, 144, 174, 159, 163, 189, 230, 204]))

# def calc_stat(listened):
#     sum = 0
#     for i in listened:
#         sum += i
#     M = (sum // 60)
#     S = sum % 60
#     return f'Вы прослушали {len(listened)} песен, общей продолжительностью {M} минут и {S} секунд.'
#
# print(calc_stat([193, 148, 210, 144, 174, 159, 163, 189, 230, 204]))

# DATABASE = {
#     'Сергей': 'Омск',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }
#
#
# def format_count_friends(count_friends):
#     if count_friends == 1:
#         return '1 друг'
#     elif 2 <= count_friends <= 4:
#         return f'{count_friends} друга'
#     else:
#         return f'{count_friends} друзей'
#
#
# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count_string = format_count_friends(len(DATABASE))
#         return f'У тебя {count_string}'
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE.keys())
#         return f'Твои друзья: {friends_string}'
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'
#
#
# def process_friend(name, query):
#     if name in DATABASE:
#         if query == 'ты где?':
#             city = DATABASE[name]
#             return f'{name} в городе {city}'
#         return '<неизвестный запрос>'
#     else:
#         return f'У тебя нет друга по имени {name}'
#
#
# def process_query(query):
#     tokens = query.split(', ')
#     name = tokens[0]
#     if name == 'Анфиса':
#         return process_anfisa(tokens[1])
#     else:
#         return process_friend(name, tokens[1])
#
#
# def runner():
#     queries = [
#         'Анфиса, сколько у меня друзей?',
#         'Анфиса, кто все мои друзья?',
#         'Анфиса, где все мои друзья?',
#         'Анфиса, кто виноват?',
#         'Коля, ты где?',
#         'Соня, что делать?',
#         'Антон, ты где?'
#     ]
#     for query in queries:
#         print(query, '-', process_query(query))
#
#
# runner()

#Урок 2. Что такое библиотеки?
# Библиотека или модуль — это набор готовых функций, объединённых общей темой.
# Чтобы получить доступ к этим функциям, нужно командой import в начале программы импортировать библиотеку.
# Это ещё называется «подключить модуль»
#from random import choice  # здесь подключите библиотеку random и дайте ей краткое имя
# answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']
# def how_are_you():
#     return choice(answers)# напишите ваш код здесь
#  print(how_are_you())

# Урок 4. Стандарт UTC
# import datetime as dt# библиотеку datetime под именем dt
# start_moment = dt.datetime(2021, 6 , 13)
# current_moment = dt.datetime(2021, 6, 27)
#
# total_time = current_moment - start_moment
#
# print(total_time)

# У каждой переменной типа данных datetime можно вызвать метод utcnow().
# Он вернёт текущий момент времени по UTC с эталонной точностью до микросекунд.
# import datetime as dt
# now = dt.datetime.utcnow()
# print(now)
# Получим текущий момент по московскому времени
# есть тип timedelta, в котором можно сохранить определённый промежуток времени
# Этот тип тоже живёт в библиотеке dt.
# А объект такого типа создаётся функцией timedelta():
# import datetime as dt
# period = dt.timedelta(hours=3) # сохраняем промежуток времени в три часа
# print(period)
# И прибавляем его к значению времени по UTC
# moscow_moment = now + period
# print(moscow_moment)
# В аргументах функции timedelta() среди прочего можно указывать days, hours, minutes, seconds, microseconds.
# import datetime as dt
# time_bottas = dt.timedelta(minutes=1, seconds=25,
#                            microseconds=273250)
# time_hamilton = time_bottas + dt.timedelta(microseconds=208860)
#
# print(time_hamilton)

import datetime as dt

# UTC_OFFSET = {
#     'Санкт-Петербург': 3,
#     'Москва': 3,
#     'Самара': 4,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Пермь': 5,
#     'Воронеж': 3,
#     'Волгоград': 4,
#     'Краснодар': 3,
#     'Калининград': 2
# }
# def what_time(city):
#     now = dt.datetime.utcnow()
#     period = dt.timedelta(hours=UTC_OFFSET[city])
#     finish = now + period
#     return finish
# print(what_time('Екатеринбург'))

# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь'
# }
#
#
# UTC_OFFSET = {
#     'Санкт-Петербург': 3,
#     'Москва': 3,
#     'Самара': 4,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Пермь': 5,
#     'Воронеж': 3,
#     'Волгоград': 4,
#     'Краснодар': 3,
#     'Калининград': 2
# }
#
# def wat_time(friend):
#     now = dt.datetime.utcnow()
#     city = DATABASE[friend]
#     friend_time = now + dt.timedelta(hours=UTC_OFFSET[city])
#     return friend_time
#
# print(wat_time('Алина'))

# Урок 5. Форматирование времени
# если хочется напечатать сообщение по-человечески, скажем: Сейчас 10:31?
# Для этого существует метод strftime()
# Его можно применить к любому объекту типа datetime и аргументом задать формат вывода времени
# import datetime as dt
# arrival_time = dt.datetime(2019, 5, 10, 19, 45)
# print('Самолёт прибывает в', arrival_time.strftime('%H:%M')) # Здесь %H означает часы, %M — минуты.
# # параметры %B — месяц, %Y — год и %S — секунды, %A — название дня недели по-английски, %U — номер недели в году.
# import datetime as dt
# # дата первого осеннего снега в Новосибирске в 2018
# first_snow = dt.datetime(2018, 9, 9)
# # дата последнего весеннего снега в Новосибирске в 2018
# last_snow = dt.datetime(2018, 5, 19)
#
# print(last_snow.strftime('Последний снег выпал в %U-ю неделю года.'))
# print(first_snow.strftime('А первый снег пошёл в %U-ю неделю.'))

# import datetime as dt  # подключите библиотеку datetime под именем dt
#
# DATABASE = {
#     'Сергей': 'Омск',
#     'Соня': 'Москва',
#     'Алексей': 'Калининград',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск',
#     'Артём': 'Владивосток',
#     'Петя': 'Михайловка'
# }
#
# UTC_OFFSET = {
#     'Москва': 3,
#     'Санкт-Петербург': 3,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Самара': 4,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Воронеж': 3,
#     'Пермь': 5,
#     'Волгоград': 4,
#     'Краснодар': 3,
#     'Калининград': 2,
#     'Владивосток': 10
# }
#
#
# def format_count_friends(count_friends):
#     if count_friends == 1:
#         return '1 друг'
#     elif 2 <= count_friends <= 4:
#         return f'{count_friends} друга'
#     else:
#         return f'{count_friends} друзей'
#
#
# def what_time(city):
#     offset = UTC_OFFSET[city]
#     city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
#     f_time = city_time.strftime("%H:%M")
#     return f_time
#
#
# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count_string = format_count_friends(len(DATABASE))
#         return f'У тебя {count_string}'
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE.keys())
#         return f'Твои друзья: {friends_string}'
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'
#
#
# def process_friend(name, query):
#     if name in DATABASE:
#         city = DATABASE[name]
#         if query == 'ты где?':
#             return f'{name} в городе {city}'
#         elif query == 'который час?':
#             if city not in UTC_OFFSET:
#                 return f'<не могу определить время в городе {city}>'
#             time = what_time(city)
#             return f'Там сейчас {time}'
#         else:
#             return '<неизвестный запрос>'
#     else:
#         return f'У тебя нет друга по имени {name}'
#
#
# def process_query(query):
#     tokens = query.split(', ')
#     name = tokens[0]
#     if name == 'Анфиса':
#         return process_anfisa(tokens[1])
#     else:
#         return process_friend(name, tokens[1])
#
#
# def runner():
#     queries = [
#         'Анфиса, сколько у меня друзей?',
#         'Анфиса, кто все мои друзья?',
#         'Анфиса, где все мои друзья?',
#         'Анфиса, кто виноват?',
#         'Коля, ты где?',
#         'Соня, что делать?',
#         'Антон, ты где?',
#         'Алексей, который час?',
#         'Артём, который час?',
#         'Антон, который час?',
#         'Петя, который час?'
#     ]
#     for query in queries:
#         print(query, '-', process_query(query))
#
#
# runner()

# Урок 4. Подробнее об URL
#user_query = 'как стать бэкенд-разработчиком'
#first_done = user_query.split(' ')
#url = 'https://yandex.ru/search/?text=' + '%20'.join(first_done)

#print(url)

# import urllib.parse
# url = 'https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE%20%D0%B5%D0%B7%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B0%20%D1%82%D0%B0%D0%BA%D1%81%D0%B8'
# #decoded = urllib.parse.unquote(url)
# first_done = url.split('=')# чтобы вычленить текст вопроса# строку по знаку = и возьмите
# list_question = first_done[1]# второй элемент получившегося списка
# question = list_question # сохраните его в переменной question
# urllib.parse.unquote(question)
#
# #на экран запрос в расшифрованном виде
# print(urllib.parse.unquote(question))

#Урок Python вместо браузера
#Общаться с серверами в интернете умеют не только браузеры.
# Вы тоже можете написать свой клиент на Python, используя библиотеку requests:
# import requests
# response = requests.get('https://ya.ru/white')
# print(response.text)  # печатаем текст запрошенной страницы

# import requests
# url = 'http://wttr.in/?0T'
# response = requests.get(url) # выполните HTTP-запрос
# print(response.text)  # напечатайте текст HTTP-ответа

# import requests
# url = 'https://wttr.in'  # не изменяйте значение URL
# weather_parameters = {
#     '0': '',
#     'T': '',
#     'M': '',
#     'lang': 'ru'# добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
# }
# response = requests.get(url, params=weather_parameters) # передайте параметры в http-запрос
# print(response.text)

# Урок : Заголовки запросов и ответов
# import requests
# response = requests.get('https://ya.ru/white')
# # вот мы узнали, что код ответа 200 и заполучили это число в свой код:
# code = response.status_code # Код HTTP-ответа (status_code) говорит о том,
# # что запрошенная страница была возвращена успешно: 200 означает Ok.
# print(f'Код ответа = {code}')
#
# # а вот мы и заголовки читаем, и выводим их форматированной строкой
# # с примечанием, каким захочется, на любом языке
# headers = response.headers#Заголовки ответа доступны как словарь headers:
# # по ключу — названию заголовка — доступно его значение.
# print(f'Тип содержимого: {headers["content-type"]}')
# print(f'Время ответа: {headers["date"]}')

#Заголовки есть не только у ответов, но и у запросов
#Когда вам понадобится передать заголовки в HTTP-запросе — соберите их в словаре,
# и передайте его как аргумент headers функции get():
# import requests
# request_headers = {
#     'Accept-Language': 'ru'  # попросим материал на русском языке
# }
#
# # сходим почитать блоги про IT, строкой передаём URL платформы habr
# response = requests.get('https://habr.com', headers=request_headers)
# print(response.text)

# import requests
# url = 'https://wttr.in'
# weather_parameters = {
#     '0': '',
#     'T': '',
#     'M': '',
# }
# request_headers = {
#     'Accept-Language':'ru'
# }
#
# # не забудьте передать параметры и заголовки в http-запрос
# # через аргументы `params` и `headers` функции get()
# response = requests.get(url, params=weather_parameters, headers=request_headers)
# print(response.text)

# Урок  Обработка ошибок

# вот функция, которая может выбросить исключение
# def calc_share(apples, friends):
#     # от строки откусываем число и приводим к типу int
#     friends_number = int(friends.split()[0])
#     return apples / friends_number

# есть 17 яблок
# apples = 17
#
# будем считать, сколько достанется каждому другу
# вызовем функцию calc_share() для разных наших знакомых,
#  с различным числом друзей
# for friends in ['7 друзей', '2 друга', '0 друзей', 'один враг']:
#      try:
#          print('Каждому достанется по', calc_share(apples, friends), 'яблока')
#      except ZeroDivisionError:
#          print('На ноль делить нельзя.')
#      except ValueError:
#          print(f'Из строки "{friends}" не получилось достать число.')

# import datetime as dt
# import requests
#
# DATABASE = {
#     'Сергей': 'Омск',
#     'Соня': 'Москва',
#     'Алексей': 'Калининград',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск',
#     'Артём': 'Владивосток',
#     'Петя': 'Михайловка'
# }
#
# UTC_OFFSET = {
#     'Москва': 3,
#     'Санкт-Петербург': 3,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Самара': 4,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Воронеж': 3,
#     'Пермь': 5,
#     'Волгоград': 4,
#     'Краснодар': 3,
#     'Калининград': 2,
#     'Владивосток': 10
# }
#
#
# def format_count_friends(count_friends):
#     if count_friends == 1:
#         return '1 друг'
#     elif 2 <= count_friends <= 4:
#         return f'{count_friends} друга'
#     else:
#         return f'{count_friends} друзей'
#
#
# def what_time(city):
#     offset = UTC_OFFSET[city]
#     city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
#     f_time = city_time.strftime("%H:%M")
#     return f_time
#
#
# def what_weather(city):
#     url = f'http://wttr.in/{city}'
#     weather_parameters = {
#         'format': 2,
#         'M': ''
#     }
#     try:
#         response = requests.get(url, params=weather_parameters)
#     except requests.ConnectionError:
#         return '<сетевая ошибка>'
#     if response.status_code == 200:
#         return response.text.strip()
#     else:
#         return '<ошибка на сервере погоды>'
#
#
# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count_string = format_count_friends(len(DATABASE))
#         return f'У тебя {count_string}'
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE.keys())
#         return f'Твои друзья: {friends_string}'
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'
#
#
# def process_friend(name, query):
#     if name in DATABASE:
#         city = DATABASE[name]
#         if query == 'ты где?':
#             return f'{name} в городе {city}'
#         elif query == 'который час?':
#             if city not in UTC_OFFSET:
#                 return f'<не могу определить время в городе {city}>'
#             time = what_time(city)
#             return f'Там сейчас {time}'
#         elif query == 'как погода?':
#             weather = what_weather(city)
#             return weather
#
#         else:
#             return '<неизвестный запрос>'
#     else:
#         return f'У тебя нет друга по имени {name}'
#
#
# def process_query(query):
#     tokens = query.split(', ')
#     name = tokens[0]
#     if name == 'Анфиса':
#         return process_anfisa(tokens[1])
#     else:
#         return process_friend(name, tokens[1])
#
#
# def runner():
#     queries = [
#         'Анфиса, сколько у меня друзей?',
#         'Анфиса, кто все мои друзья?',
#         'Анфиса, где все мои друзья?',
#         'Анфиса, кто виноват?',
#         'Коля, ты где?',
#         'Соня, что делать?',
#         'Антон, ты где?',
#         'Алексей, который час?',
#         'Артём, который час?',
#         'Антон, который час?',
#         'Петя, который час?',
#         'Коля, как погода?',
#         'Соня, как погода?',
#         'Антон, как погода?'
#     ]
#     for query in queries:
#         print(query, '-', process_query(query))
#
#
# runner()

# Урок: Зачем нужны фреймворки
