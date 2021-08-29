"""
ООП
    1. + и - механизмв
    2. классы. объекты. атрибуты
    3. конструкторы. методы
    4. локал. и глобал. переменные
    5. модификаторы доступа
    6. икапсулирование, как безопасность от внешнего воздействия (это принцип ООП)
    7. наследие
    8. множественное наследие
    9. полиморфизм
"""
"""
1. 
+ поаторное использование кода
+ читаемость и гибкость кода
+ ускоренный поиск ошибок и их исправление
+ повышение безопасности проекта
+ модульность (для каждого класса принято отводить отдельный ф. и в нем работать) 
- хорошее понимание предметной области
- хорошее представление структуры приложениия
- сложность разбития проекта на классы
- сложность в модификации проекта
"""
# этот ф. будет использоваться как ф. для нового класса (описывающий человека)
# class - определяем и с большой буквы задаем имя
#class Person: # ниже атрибуты - свойства которые могут описывать любого человека. Общее описание, создаем шаблон
    #hands_count = 2
    #legs_count = 2
    #sex = None # все это атрибуты клс.Person
    #hands_count = 2 # общий атрибут для всех экз.клс
    # если изменить это значение в конструкторе, то оно перейдет ко всем остальным экз.клс.Общие парам. по шаблону Person
                                                                  # это значение отриб по умолчанию
#    def __init__(self, eye_color, hair_color, heigh, weight, name, education, sex='Famale'): # это конструктор,
        # вызывается когда создается новый экз.клас. Прописываются атрибуты экзе-ра - как аргументы
        # скрыт от глаз разраб -ка. Вызывается автматически
        # sex, eye_color, hair_color, heigh, weight - это экземпл.клс. Через self, ниже сохраняем атрибуты экз.
        # когда нужны какие-то описвтельные части для конкретного экз.клс.
        # так можно все необходимые атрибуты передать. И атриб клс.не обязательнвя часть
        # self.sex = sex # это втрибуты экз.клс
        # self.eye_color = eye_color
        # self.hair_color = hair_color
        # self.heigh = heigh
        # self.weight = weight
        # self.name = name
        # self.education = education # внес education в атрибут и конструктор
        # #Person.hands_count += 1 # здесь меняем атрибут клс при каждом создании экз.клс
    #     print(f'это {name}, у него/нее {eye_color} глвза и {hair_color} волосы')
    #
    #
    # def person_sleep(self):# создали метод - это функция принадлежашая Person клс, отступы!
    #     # self я передаю, что бы обращаться к атрибутам экз.клс из метода -даю доступ
    #     print(f'Person {self.name} sleeps')
    #
    # def person_eat(self): # self = Oleg, Anna
    #     print(f'Person {self.name} eats')
    #
    # def person_wake_up(self):
    #     print(f'Person {self.name} wakes up')

    # в род.клс добавили еще 1 метод, при уже созданном дочернем
    # метод person_play автоматически перемещен в дочерний клс. Есть по умолчанию. Вызываю ниже
#    def person_play(self):
#        print(f'Person {self.name} plays')

#print(Person.hands_count)
# создан шаблон, по нему можно создать обьект или (по другому экземпляр клс)
#Oleg = Person('black', 'black', 190, 95, 'Олег', 'Male') # self указанный выше в функуц, это ссылка на Oleg
#print(Oleg.name) # принт значение атрибута моего экз.клс
#print(Person.hands_count)
#print(Oleg.info)

# hands_count = 2  - это атрибуты класса
#     legs_count = 2  - они присутствуют и в экземплярах клс.
#     sex = None
                                        # Famale - по умолчанию как значение атриб, потому у Anna можно не прописывать
#Anna = Person('black', 'blond', 190, 95, 'Анна') # конкретные параметры для обектов - экземпляров клс.
#print(Anna.sex) # атрибуты экземпляра клс - то что описывает oleg и Anna -прописывается в конструкторе
#print(Person.hands_count)
# указываюися в экз.клс как параметры позиц или именнован. В порядке записвнном в клас
# в момент объявления экз.клс, указываются все значения атрибутов - аргументов

#print(Person.hands_count) # Для обащения к атрибутам класса (имя клс.название атрибута)
#print(Person.person_sleep()) # для обращения к методу

"""переиспользуем код 
Если вызываем свой конструктор в новом насдедуемом клс - перегрузка
Перезагружается метод:
- если будут метод стаким же именем - он перетерается
- логика нового, дочернего клс. осущетсвится в конструкторе
- для примера person_eat, добавлено где он ест
"""

#class WorkingPerson(Person): # У этого клс должны быть теже атрб. что и у обшего клс.
    # это дочерний клс. наследукмый от родительского Person
#    def __init__(self, eye_color, hair_color, heigth, weight, name, experience, education, sex): # education добавлен
        # experience вписали новый атрибут в внаследуемый конструктор
        # принимает теже атриб. от конструктора выше
        # это как append для функ.метолов клс.
#        super().__init__(eye_color, hair_color, heigth, weight, name, education, sex='Male') # перегрузка конструктора + education
        #Person().__init(self, ....) другая запись перезагрузки родительского клс._
#        self.experience = experience # установили новый отрибут в ноывый наследуемый экз.
    # в этом дочернем клс 2 повторяющихся метода - конструктор
    # и перезаписанный person_eat
    # это расширило логику родительского клс.
    # конст-ор невозвращает, нет return
    # в методах можно return
    # def person_eat(self, place):
    #     print(f'Person {self.name} eats in {place}')
    #
    # def person_go_to_work(self): # + доп. функционал - ходит на работу
    #      print(f'person {self.name} goes to work')
    #      # Добавление доп.характеристик в WorkingPerson - стаж в конструктор
    #
    # def get_info(self):
    #     print(f'{self.name} человек работаюший')
# + еще класс наследуемый от род. Не перегружаем конструктор. Разница только в + методах
# class HomeStayPerson(Person):
#     def person_cook(self, cooking):
#        print(f'person {self.name} cooks {cooking}')
# эти методы присущи только этому клс.
# доступны только экз.клс созданному на основе HomeStayPerson
#     def person_cleaning(self):
#         print(f'person {self.name} cleans the room')
#
#     def get_info(self):
#         print(f'{self.name} не работвюший чел (дома сидит)')
# Множественное наследование - клс содержаший в себе все методы от род + доч.
# class UniversalPerson(WorkingPerson, HomeStayPerson): # наследуется от 2ух доч.клс. Первый указан клс. в арг. - главнее
#     pass
#
#
#
# #Filipp = WorkingPerson('black', 'brown', 190, 90, 'FIlipp', 10, 'PhD', sex='Male') # Так же передать все атрибуты, они унаследованы
# при создаании экз.тоже внес education - значение PhD
# print(Filipp.experience) #обращение к новому атрибуту
# Filipp.person_eat('MacDonalds') # вызывая здесь eat - идем по логике дочернего клс + обязвтель но указать новый атрибут - MacDonalds
# Filipp.person_sleep()
# Filipp.person_go_to_work()
#Filipp.person_play()
# Filipp это экз. клс. WorkingPerson
# WorkingPerson унаследован от Person
# значит у есть все методы клс.Person (sleep, wake_up, play)
# за исключением перезаписанных eat(place - добавленый арг.)
# при вызове person_eat обязанность указать ('MacDonalds') - значение атриб (место где ест)
# если в род.клс мы вносим изменения, то изменяем и доч. клс тоже

#Anna = Person('black', 'brown', 190, 90, 'Anna', 'school', sex='Female') # это обычный человек, от родиткльского клс.
# Anna.person_eat()
#
# Svetlana = HomeStayPerson('blue', 'brown', 160, 85, 'Svetlana', 'school', sex='Female') # тот же конст. что и в род.клс
# Svetlana.person_cook('dinner') # ей доступны методы HomeStayPerson
#Svetlana.person_cleaning()
# + доступны все методы исход.род.клс.
# Svetlana.person_eat()
# Svetlana.person_sleep()

# экз.клс универсального чел
#Nikola = UniversalPerson('black', 'brown', 190, 90, 'Nikola', 10, 'PhD', sex='Male')
# важно соблюдать порядок - начало от главного клс
# __init__ происходит по 1 указ клс. При одинаковых методах - гпавный берется от родителя
# Nikola.person_eat("Home")
# Nikola.person_go_to_work()
# Nikola.person_cleaning()
# Nikola.person_play()
# т.к.WorkingPerson, HomeStayPerson унаследованы от Person - род.клс + доступны методы и из него
#Nikola.get_info() # этот метод одиноковый в двух дочерних клс
# метод WorkingPerson отработал
"""
локальные перемен - атриб. объявлены в нутри метода и работают в нутри него. 
глобвльные переменные - как атриб клс, имею к ним доступ
+ модификаторы доступа
"""
# class Person:
#     def __init__(self, name, surname, phone, login, password):
#         self.name = name # self-это публичный атриб. Доступ через .
#         self.surname = surname
#         self.phone = phone
#         self._login = login # private # условно защищенный атриб - на уровне договоренности
#         # если есть _ должен использоваться в этом классе или дочерних клс. Где-то из вне не меняем
#         # можно вызывать, что-то возврашать
#         self.__password = password # Protected # полностью приватный - внутрений атриб.
#         # защищен от внешнего обрашения, попытки переосвоения
#
#     def get_login(self):
#         return self._login
#
#     # с ними можно работать только в нутри класса
#     def __get_password(self):
#         return self.__password # вернули через метод внутрений, зашишенный атриб. Тогда в экз.клс можно получить значение
# # чтобы изменить значение мне нужно прописать в методе
#     def set_password(self, new_password): # 2ым арг. задаем новый пароль
#         self.__password = new_password # значение нового пароля сохранили
#         self.__get_password() # могу вызвать защищенный метол здесь
# тоже работает и с методами
# def __get_password - полностью защищеный метод
# доступен только в нутори другого метода
class Person:
    def __init__(self, name, surname, phone, login, password):
        self.name = name # self-это публичный атриб. Доступ через .
        self.surname = surname
        self.phone = phone
        self._login = login # private # условно защищенный атриб - на уровне договоренности
        # если есть _ должен использоваться в этом классе или дочерних клс. Где-то из вне не меняем
        # можно вызывать, что-то возврашать
        self.__password = password # Protected # полностью приватный - внутрений атриб.
        # защищен от внешнего обрашения, попытки переосвоения

    def get_login(self):
        return self._login

    # с ними можно работать только в нутри класса
    def __get_password(self):
        return self.__password # вернули через метод внутрений, зашишенный атриб. Тогда в экз.клс можно получить значение
# чтобы изменить значение мне нужно прописать в методе
    def set_password(self, new_password): # 2ым арг. задаем новый пароль
        self.__password = new_password # значение нового пароля сохранили
        self.__get_password() # могу вызвать защищенный метол здесь
# тоже работает и с методами
# def __get_password - полностью защищеный метод
# доступен только в нутори другого метода

# уровни доступа к моим атриб.экз.клс и методов клс. в том числе
Anna = Person("Anna", "Danilova", "223-322", "anna-dan", "Qwerty")
print(Anna.name) #публичный атриб. - через имя экз.клс (просим вернуть имя)
# это имя я могу поменять, отпринтовать...
Anna.name = 'Не Анна'
print(Anna.name)
Anna._login = "cnsdas"
print(Anna._login)
print(Anna.get_login()) # публичный атриб.- так же и для метода экз.клс
print(Anna.get_password())
# злесь проверяем и меняем пароль
print(Anna.get_password())
Anna.set_password("Qwerty12345")
print(Anna.get_password())

# уровни доступа к моим атриб.экз.клс и методов клс. в том числе
Anna = Person("Anna", "Danilova", "223-322", "anna-dan", "Qwerty")
print(Anna.name) #публичный атриб. - через имя экз.клс (просим вернуть имя)
# это имя я могу поменять, отпринтовать...
Anna.name = 'Не Анна'
print(Anna.name)
Anna._login = "cnsdas"
print(Anna._login)
print(Anna.get_login()) # публичный атриб.- так же и для метода экз.клс
print(Anna.get_password())
# злесь проверяем и меняем пароль
print(Anna.get_password())
Anna.set_password("Qwerty12345")
print(Anna.get_password())
print(Anna.__get_password()) # будет ошибка, метод не доступен