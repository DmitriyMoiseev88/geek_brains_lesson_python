#Задание от третьей лекции 3.1
def div(*args):
    try:
        arg1 = int(input("Input dividend "))
        arg2 = int(input("Input divider "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"

    return res

'''
if arg2 != 0:
    return arg1 / arg2
    else:
    print("Wrong number! Devider can't be null")
'''


print(f'result  {div()}')

#Задание от третьей лекции 3.2
'''
    name = input('enter name')
    surname = input('enter surname')
    year = int(input('enter year'))
    city = input('enter city')
    email = input('enter email')
    telephone = input('input telephone')
'''
def my_func (name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Frolov', name = 'Sergey', year = '1990', city = 'Syzran',
               email = 'error@mail.ru', telephone = '8-903-300-99-87'))

#Задание от третьей лекции 3.3
def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(f'Result - {my_func(int(input("enter first argument ")),int(input("enter second argument ")),int(input("enter third argument ")))}')

#Задание от третьей лекции 3.4
'''
 Программа принимает действительное положительное число x
 и целое отрицательное число y. Необходимо выполнить возведение
 числа x в степень y. Задание необходимо реализовать в виде функции
 my_func(x, y). При решении задания необходимо обойтись без встроенной
 функции возведения числа в степень.
'''
def x_pow (x, y):


#Задание от третьей лекции 3.5
def my_sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')

my_sum()


# Задание от третьей лекции 3.6
'''
    Реализовать функцию int_func(), принимающую слово из маленьких
    латинских букв и возвращающую его же, но с прописной первой буквой.
    Например, print(int_func(‘text’)) -> Text.
    Продолжить работу над заданием. В программу должна попадать
    строка из слов, разделенных пробелом. Каждое слово состоит
    из латинских букв в нижнем регистре. Сделать вывод исходной
    строки, но каждое слово должно начинаться с заглавной буквы.
    Необходимо использовать написанную ранее функцию int_func().
'''

def int_func(*args):
    word = input("Input words ")
    print(word.title())
    return

int_func()
