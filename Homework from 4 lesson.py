"""
1.Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
    В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, productivity, rate_per_hour, bonus = argv
print("Name of script: ", script_name)
print('Productivity, hours: ', productivity)
print('Rate_per_hour: ', rate_per_hour)
print('Bonus: ', bonus)
print('Salary: ', int(productivity) * int(rate_per_hour) + int(bonus))

"""
2. Из списка чисел вывести эллементы, значения которых больще предыдущего элемента.
    -Элементы подходящие под условие, оформить в виде списка.
    -Использовать генератор.
"""
def my_func():
    my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55 ]
    print(f'Исходный список: {my_list}')

    result_list = [my_list[index] for index in range(1, len(my_list)) if my_list[index] > my_list[index-1]]

    print(f'Результат: {result_list}')

if __name__ == "__main__":
    my_func()

"""
3. Для чисел в приделах от 20 до 241 найти числа, кратные 20 и 21.
    Решение в одну строку и используя range и генератор.
"""
result = print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0 ])

"""
4. Оприделить элементы списка не имеющие поыторений.
    Оформить результат в массив. Элементы вывести в порядке их следования
    Использовать генератор
"""
from random import randint

# source_list = [randint(0, 10) for i in range(20)]
source_list = [2, 2, 2, 7, 23, 1, 48, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Исходный список: {source_list}')

result = [el for el in source_list if source_list.count(el) == 1]
print(f'В списке не повторяются числа: {result}')

"""
5. Сформировать список из четных чисел, от 100 до 1000 (вкл. границы)
    используя range() и генератор. Получить результат вычисления произведения всех элементов.
    Использовать reduce()
"""

from functools import reduce

sourse_list = [el for el in range(100, 1001) if el % 2 == 0]

result = reduce(lambda x, y: x*y, sourse_list)
print(result)

"""
6. Реализовать два скрипта:
    a) итератор, генерирует целые числа, нвчпло с указаннгоо.
    b) итератор, повторяющий элементы некоторого списка, определенного заранее.
    - Использовать count() и  cycle() модуль itertools.
    - внимание на завершение цикла.
"""
from itertools import count, cycle
import sys

start_from = 10
iterable = "ABCDEF"
iterations_count = 0

def integer_generator(start_from):
    for el in count(start_from):
        if el > start_from + 10:
            break
        yield el

for el in integer_generator(15):
    print(el)

# метод cycle
for el in cycle(iterable):
    if el == iterable[0]:
        iterations_count += 1
    if iterations_count < 3:
        print(el)
    else:
        break

"""
7. Построить генератор факториала числа с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
#
from functools import  reduce
from itertools import count

def fact(n):
    for i in count(1):
        if i <= n:
            result = reduce(lambda x, y: x*y, range(1, i+1))
            yield result
        else:
            break

for el in fact(10):
    print(el)


# фариает короче:
# def fact(n):
#     result = 1
#     for i in count(1):
#         if i <= n:
#             result *= i
#             yield result
#         else:
#             break
#
# for el in fact(10):
#     print(el)