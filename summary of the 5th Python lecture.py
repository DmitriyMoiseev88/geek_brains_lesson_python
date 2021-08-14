# """
#     Работа с файлами
#     1.Чтение и запись
#     2.Менеджеры контекста
#     3.Вывление ошибок при работе с файлами
#     4.Режим доступа к файлу
#     5.Параметры файловаго объекта
#     6.Определение позиции указателя в файле
#     7.Print в файле
#     8.Модуль json
#     9.Модуль shutil
#     10.Модуль sys
# """
#file_obj = open('my_file', 'r')
# По умолчпнию, если mode не указан - то режим на чтение
#print(file_obj.read()) # чтение ф. от начала до конца. Читает как string
#file_obj.close() # Файл обязательно закрыть после действий
# print(file_obj.read(10)) указываем кол-во байт на прочтение
# print(file_obj.read(10)) # указывая еше 10, прочтет следущие 10 байт
#print(file_obj.readline()) # считывает файл построчно, поочередно
# print(file_obj.readlines()) # все строки, упакует их как элем. списка
# for line in file_obj.readlines():
#     print(line)
# file_obj.close()
# что бы открыть ф. в бинаоном представлении
# file_obj = open('my_file', 'rb')

# """Переносы строки, Табуляция"""
# tab = "Антон\tпривет"
# print(tab)
# tab = r"Антон\tпривет" # взять строку так, как напечатал пользователь

# Открытие файла на запись
#file_obj = open('my_file', 'w')
# методы
#file_obj.write('Что-то можно записать в ф. используя "w"') # если была запись, то перезапишется.
# Еслм ф. не сущуствует, создаст с записью
#file_obj.close()

#file_obj = open('my_file', 'r+') # расширяет режим чтония, могу использовать метод .write - для записи тоже
# так же перезапишет запись повверх прежней
#file_obj = open('my_file_write', 'w +')
# + позволяет исподьзовать методы, не применимые без него
#file_obj.writelines(['мороз\n', 'и солнце\n', 'день чудемный\n'])
# принимает список строк на запись
#file_obj = open('my_file_write', 'wb') # на запись в бинарном виде

# режим редактирования x, на запись - ругается если запись идет в существующий ф.
# если такого файла нет, создаст
# file_obj = open('my_file' 'x')
# line = file_obj.read()
# file_obj.close()

# метод a - открыть ф. на дозапись в конец строки
# file_obj = open('my_file' 'a') # если ф. не сущ-ет, создаст и запишет
# file_obj.write(" строка")
# file_obj.close()

# Менеджер контекста - варианты работы с ф.
# with open('my_file', 'a') as file_obj:
# # не требует закрытия ф. В скобках имя файла, mode - что хотим с ним сделать, as - переменная в которую кладем его
#     file_obj.write(" строка")
#
# with open('my_file', 'w') as file_obj: # запись с помошьб print()
#     print('с начало то, что нужно записать', file=file_obj) # обязательно указать чрез file - ф. в который записываеи
#
# # работа с ненсколькими ф.
# with open('my_file', 'w') as file_obj, open('my_file_1', 'r+') as file_obj_1:
# # Без with продолжаем указывать...таже запись к другим ф. в другую переменую
#     content = file_obj_1.writelines(['мороз\n', 'и солнце\n', 'день чудемный\n'])
#     print(content, file=file_obj)
# # параметры файлового объекта, смотрим через принт
#     print(file_obj.closed) # лоничкское значение True или (False - открыт или открыт. Открыт пока работаем в менеджере контекста)
#     print(file_obj.mode) # режим в котором открыт ф.
#     print(file_obj.name) # имя файла на которое ссылается переменнвя
#
#     file_obj_1.read(2) # читаем 2 байта (на каждый эллем. по 1 байту, указывать нечетное колл-во - ошибка)
# # указывать encoding="utf-8", что бы не было ошибки. На английском языке метод read - возвращает не четное кол-во
#     print(file_obj.tell()) # покажет на коком байте остановился курсор
#     print(file_obj_1.seek(3, 0)) # сдвиг курсора на 3 байта 0 - от ночала (1- от текущей позиции: 2- от концв)


import os
# """
# Модули расширяющие возможности функций + помощь в работе с файлами
# remove() - удаление ф. из дериктории
# rename() - переименовывает ф.
# listdir() - ф. в указанной директории
#
# os.path.basename() - возврат названия ф. пути, стаит последеим
# os.path.dirname() - возврат часть каталога пути, выделяет имя директории
# os.path.exists() - провеврка присутствия ф. (ставится последним в указании пути)
# os.path.isdir(), os.path.isfile() - проверка объекта на ф. или папку
# os.path.join() - объединяет несколько путей, выйдет новая директория
# os.path.split() - разделение пути на кортеж, содержит и путь до каталога, и имя файла
# """
#os.rename('text', 'me_text')

# content = os.listdir(path='.')
# print(content)
# подмодули
#print(os.path.basename("/usr/local/bin/python3.9 /Users/macbook/PycharmProjects/geek_brains_lesson_python/summary of the 5th Python lecture.py"))
#print(os.path.dirname("/usr/local/bin/python3.9 /Users/macbook/PycharmProjects/geek_brains_lesson_python/summary of the 5th Python lecture.py"))
#print(os.path.exists("/usr/local/bin/python3.9 /Users/macbook/PycharmProjects/geek_brains_lesson_python/summary of the 5th Python lecture.py"))
#print(os.path.isdir("/usr/local/bin/python3.9 /Users/macbook/PycharmProjects/geek_brains_lesson_python/summary of the 5th Python lecture.py"))
#print(os.path.isfile("/usr/local/bin/python3.9 /Users/macbook/PycharmProjects/geek_brains_lesson_python/summary of the 5th Python lecture.py"))
#print(os.path.join('', '' ))
#print(os.path.split("/usr/local/bin/python3.9 /Users/macbook/PycharmProjects/geek_brains_lesson_python/summary of the 5th Python lecture.py"))
#os.remove("my_file")

import json
# """
# json - универсальная нотация, понимает все языки при обмене информации. Это хранение данных
# сериализация - процесс преобразования в json
# """
# dumps - сериализация в json строку
#my_dict = {'Apple': 150, 'Pineaple': 300, 'Lemon': 60}# словарь
# json_str = json.dumps(my_dict) # в таком виде могут принимать другие прог-мы, знающие нотацию json
# print(json_str)
# print(type(json_str))

#json объект - json.dump()
# 1ый арг. - что я преобразую, 2ой - в какой ф. это помещаю
# with open("new.json", "w") as file:
#     json.dump(my_dict, file) # это json объект сохраненый в ф.

# обратный процесс Десириализация - из json в питон
# with open("new.json") as file: # открыли объект json
#     data = json.load(file) # метод load - в питон. словарь

# json.loads() - Десириализация строкового типа json. s - в окончании метода говорит о строковом типе
# data = json.load(my_json_string)
# print(data)# будет строка
#
# import shutil
# """
# модуль для выполнения операций над ф. и папками:
# копироапние. перемещение, удаление.
# может пригодится при написании десктопного приложения - реализация логики приложения
# shutil.copy() - копирование содержтмого или текста исходного ф. в конечный ф.
# shutil.copyfile() - копирование ф. не копирует методанные
# shutil.copyfileobj() - копирование содержимого ф. объекта в другой
# shutil.move(file, path) - перемещение ф. или директории в указанную директорию
# shutil.rmtree(path) - удаление директории
# """
# shutil.copy("my_text", "my_copy_text") # создаст новый ф. my_copy_text, если не было
# shutil.copyfile("my_text", "my_copy_text_2") # сдесь работа конкретно с файлами
#
# src_file_obj = open("my_text", "rb")# достаем ф. объект в переменную
# targ_file_obj = open("my_copy_text_2", "wb")
# shutil.copyfileobj(src_file_obj, targ_file_obj) # копирование фай-ых объектов
# src_file_obj.close()
# targ_file_obj.close()
#
# shutil.move("имя папки", "путь до другой директории")
# shutil.move("путь до нужной директории", "имя папки, файла") # перемещение обратно
#
# shutil.rmtree(path) # удаление директории

#import sys, time
#print(sys.path) # директории которые есть, от вызванной поднимается выше
# print(sys.executable) # где лежит бинарный ф. с интерпритатор
# print(dir(sys)) # все внутренние пара-ры нашего модуля
# sys.exit(0) # закрытие модуля, 0 - это успешное. Нижний print не пройдет
# print("это не отпринтуется")


# """выводит по буквенно в стандартный поток вывода мой текст
# time.sleep - дает необходимую задержку
# не используется принт - sys.stdout.write() -стандартный поток вывода
# """
# def teleprint(*args, delay=0.05, str_join=" "): # позиционные и имнованные арг.
#     text = str_join.join(str(x) for x in args)
#     n = len(text)
#     for i, char in enumerate(text, 1):
#         if i == n:
#             char = f'{char}\n'
#         sys.stdout.write(char) # станд.поток выводв - выводит на экран
#         time.sleep(delay)

# teleprint("печать с задержкой!", 10, 12.5, "Super!!!", delay=0.05)

# стандарт. поток ввода - что-то склавиатуры
# for line in sys.stdin: # для каждой строки того, что я ввел с клавиатуры
#     print(line.rstrip('\n')[::-1])
#     sys.exit(0)

# поток стандартныйх ошибок sys.stderr
# try:
#     10 / 0
# except ZeroDivisionError:
#     sys.stderr.write('Exception occuted:\n')
#

