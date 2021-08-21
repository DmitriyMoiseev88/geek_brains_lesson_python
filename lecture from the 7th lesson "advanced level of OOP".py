# import math
#
#
# class Person:
# атрибут клс, доступен для всех пораждаемых объектов, экз.этого клс
#     phone = '223-332'
# метод конструктор
# все что через self, это атриб.экз клс.
#     def __init__(self, name, surname, login, password):
#         self.name = name # public
#         self.surname = surname
#         self._login = login # protected
#         self.__password = password # privat

# методы класса

# через self передаем ссылку на экз.класса
#     def __get_password(self):
#         return self.__password

# def set_password(self, new_password):
#     self.__password = new_password
#     print(self.__get_password())

# def person_play(self):
#     print(f'Person {self.name} plays')
# экз. клс от род.Person
# Anna = Person('Anna', 'Danilova', 'anna-part', 'Qwerty')
# вызываем метод

# Anna.set_password('Qwerty12345')
# обращение к глоб перемен
# print(Anna.phone)


# class Student:
# def __new__(cls, *args): # ссылка на клс
#     print('создан новый экз.клс')
#     cls.__init__(cls, *args) # перегрузили

# def __init__(self, id, name):  # срабатывает при создании объектов, соот-ет конструктору объектов клс.
#     self. id, self.name = id, name
#     print('инициализирован экз.клс') # print для наглядности работы метода, student = Student(1, "Dimon")

# срабатывает при удалении объекта соот-ет деструктору объектов клс.
# перегружаем деструктор
# def __del__(self): # будет вызван автоматически системой, когда ф. закончит раб. - мусоросборник
#     print('экз.клс. удален')

# преобразует объект к строке, срабатывает при передаче объекта функциям str() и print()
#     def __str__(self):
#         return f'наш студент {self.name}' # print(student)

# срабатывает при обрашении к экз.клс как к функц.
#     def __call__(self): # student()
#         print('Меня позвали')


# student = Student(1, "Dimon")
# del student # явная пропись удаления
# print(student)
# student()

# __setattr__() # срабатывает при присвоении значения атриб.объек
# __getitem__() # срабатывает при извлечении элм. по индексу

"""
делаем перегрузку когда нужно изменить какуюто логику неявных методов, указвнных выше.
def __del__(self): - например при таком методе составить лонику запроса о конечном решении на удалении
- не можем складывать списки, только канкотиницией
- ниже клс. для этой задачи и прегрузка метода
"""
# import math
#
# class My_init():
#
#     def __init__(self, init_list):
#         self.init_list = init_list
#
#     def __str__(self):
#         return str(self.init_list)
# метод = сложению. перегружаю логику под задачу
#     def __add__(self, other):
#         result_list = []
#         for i, j in zip(self.init_list, other.init_list):
#             result_list.append(i+j)
#         return My_init(result_list) # новый экз.клс.


# складываем 2 экз.клс
# my_list_1 = My_init([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# my_list_2 = My_init([1, 2, 3, 4, 5, 6, 4, 3, 2, 1, 0]) # other - на него ссылка
# print(my_list_1 + my_list_2)
import math

# class My_vector2D:
#     def __init__(self, x, y): # перегружен конструктор координ-ми x, y
#         self.x = x
#         self.y = y
#
#     def __str__(self):# при попытке print или обращению к элл.экз
#         return 'Vector2D({}, {})'.format(self.x, self.y) # выдаст сформированную строку
# перегрузка оператора сложения
#     def __add__(self, other):
#         return My_vector2D(self.x + other.x, self.y + other.y )
# когда есит +=
#     def __iadd__(self, other):
#         self.x += other.x
#         self.y += other.y
#         return self
# перегузка оператора вычитания (-)
# def __sub__(self, other):
#     return My_vector2D(self.x - other.x, self.y - other.y)
#
# def __isub__(self, other):
#     self.x -= other
#     self.y -= other
#     return self
# умножение
#     def __mul__(self, other):
#         return My_vector2D(self.x * other.x, self.y * other.y)
# вычисление длиины вектора через math.hypot(x2 , y2) - вычисленная длина вектора
#     def __abs__(self):
#         return math.hypot(self.x, self.y)
# когда пытаемся сконвертировать экз.клс в bulзначение
#     def __bool__(self):
#         return self.x != 0 or self.y != 0

# возвращение с отрицательным знаком вектора
#     def __neg__(self):
#         return My_vector2D(-self.x, -self.y)

# x = My_vector2D(3, 4) # создан новый экз.клс x
# print(x) # __str__(self)
# print(abs(x)) # коркень из суммы x2, y2
# y = My_vector2D(5, 6) # создан новый 2ой экз.клс y
# print(x + y) # __add__(self, other):
# print(x - y) # __neg__(self):
# print(-x)
# x += y # __iadd__(self, other):
# print(x)
# print(bool(x))
# z = My_vector2D(0, 0) # создан новый 3ий экз.клс z
# print(bool(z))
# print(-z)

# class Vehicle:
#     def print_details(self):
#         print("Это род-ий метод и клс Vehicle")

# Создание клс, наследует Vehicle
# class Car(Vehicle):
#     def print_details(self):
#         super().print_details()
#         #Vehicle.print_details(self) # или так вызвать род.метод
#         print("Это доч-ий метод и клс Car")

# Создание клс Cycle, наследует Vehicle
# class Cycle(Vehicle):
#     def print_details(self):
#         print("Это доч-ий метод и клс Cycle")
#
# my_vehicle = Vehicle()
# my_car = Car()
# my_car.print_details()

"""
Декораторы
 - это функ-ии позволяюшие обернуть друг функ. расширения их
  функциональности без непосредственного изменения ее кода
"""

# def higher_other(func):
#     print('Полученная фун. {} в качестве арг-та'.format(func))
#     func()
#     return func
# описание логики декоратора
# def decorator_function(func):
#     def wrapper(*args, **kwargs):
#         print('функция обертка')
#         print('оборачиваемая функция: {}'.format(func))
#         print('выполняем обернутую функцию ...')
#         func(*args, **kwargs)
#         print('выходим из обертки')
#     return wrapper

# def hello_world():
# print('Hello world')

# decorator_function(hello_world)()
# таккая догика записывактся так:
# @decorator_function # @ - означает, что функ. hello_world() передаю как арг в decorator_function
# def hello_world(world):
#     print(f'Hello {world}')
# hello_world('world')


# @decorator_function
# def check_smth():
#     print('A + B')
# check_smth()

# декоратор обрабатываюший ошибка
# def error_wrapper(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except ZeroDivisionError:
#             print('деление на ноль')
#         except TypeError:
#             print('неверный тиа вводных данных')
#     return wrapper
#
# @error_wrapper
# def division(a, b):
#     print(a/b)
#
# division(1, 0)

"""
Абстрактные методы. Интерфейс
    Интерфейс - описывает поведение объекта
    Абстрактные методы - контроль поведения клс.наследников,
    диктует структуру - не забыть #перегрузить методы"
"""
# from abc import ABC, abstractmethod
# этот клс родителя шаблон, понему нельзя создать шаблон
# нужно от него унвследоваться и описать логику
# class MyAbstractClass(ABC):
#     @abstractmethod # навешивавется встроенный дек. из модуля ABC
#     def my_method_1(self):
#         pass
# # если я наследуюсь от MyAbstractClass, должны быть здешние методы
# # их нужно переопределить
#     @abstractmethod
#     def my_method_2(self):
#         pass
#
# class MyClass(MyAbstractClass):
#     def my_method_1(self): # методы переопределены
#         pass
#     def my_method_2(self): # небудет род.метода - ошибка
#         pass
#
# mc = MyClass()

"""
декоратор @property - дает возможность вызывать метод - функцию,
(Anna.get_password), как функц. с атрибутом
"""
# class Person:
#     def __init__(self, name, surname, phone, login, password):
#         self.name = name
#         self.surname = surname
#         self.phone = phone
#         self._login = login
#         self.__password = password
#
#     def get_login(self):
#         return self._login
#
#     @property # после навешивания вызывается как отрибут
#     def get_password(self):
#         return self.__password
#
#     def set_password(self, new_password):
#         self.__password = new_password
#         self.__get_password()

"""
интерфейс итератора
итератор - может перебирать поштучно (ленивый гениротор)
не явно реализован в цикле for in - перебирает коллекцию
работает в листкомприхеншенс, в функ.map, filter
генератор - это частичная реализация итератора
iter - это метод к которому могу пременить функ next 
пошагоаого извлечения эллем из коллекции

объекты которые не можем перебирать
"""
#
# my_list = [30, 105.6, 'text', True]
# my_iterator = iter(my_list)
# for el in my_list:
#     print(el)

# print(my_iterator)
# print(type(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator)) # ошибка StopIteration

"""
композиции - в одном клс. могу вызывать функ.другого клс
@staticmethod - если хотим что бы метод клс не принимал ссылки на объекты
"""


class WindowDoor:
    def __init__(self, wd_len, wd_height):
        self.square = wd_len * wd_height

class Room:
    def __init__(self, len_1, len_2, height):
        self.square = 2 * height * (len_1 + len_2)
        self.wd = []

    def add_win_door(self, wd_len, wd_height):
        self.wd.append(WindowDoor(wd_len, wd_height))

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square


r = Room(7, 4, 3.7)
print(r.square)
r.add_win_door(2, 2)
r.add_win_door(2, 2)
r.add_win_door(2, 2)
print(r.common_square())
