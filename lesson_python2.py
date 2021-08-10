# Задание 1
# a = 10
# b = 15
# print("Переменные a и b - ", a, b)
# string1 = input("Введите первую строку ")
# number1 = int(input("Введите первое число "))
# string2 = input("Введите вторую строку ")
# number2 = int(input("Введите второе число "))
# print("Введеные значения - %10s %5d %10s %5d" % (string1, number1, string2, number2))


# # Задание 2
# current_second = int(input("Введите время в секундах "))
# hours = current_second // 3600
# minutes = (current_second - hours * 3600) // 60
# seconds = current_second - (hours * 3600 + minutes * 60)
# print(f"Время в формате чч:мм:сс   {hours:02d} : {minutes:02d} : {seconds:02d}")

# Задание 3
# n = int(input('Введите число n: '))
# n1 = str(n)
# n2 = n1 + n1
# n3 = n1+ n1 + n1
# number_sum = n + int(n2) + int(n3)
# print('Итог:', number_sum)

# Задание 4
# n = abs(int(input("Введите целое положительное число ")))
# max = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > max:
#         max = n % 10
#     if n > 9:
#         continue
#     else:
#         print("Максимальное цифра в числе ", max)
#         break

# Задание 5
# profit = float(input("Введите выручку фирмы "))
# costs = float(input("Введите издержки фирмы "))
# if profit > costs:
#     print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
#     workers = int(input("Введите количество сотрудников фирмы "))
#     print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
# elif profit == costs:
#     print("Фирма работает в ноль")
# else:
#     print("Фирма работает в убыток")

# Задание 6
# a = int(input("Введите результаты пробежки первого дня в км "))
# b = int(input("Введите общий желаемый результат в км "))
# result_days = 1
# result_km = a
# while result_km < b:
#         a = a + 0.1 * a
#         result_days += 1
#         result_km = result_km + a
# print(f"Вы достигнете требуемых показателей на %.d день" % result_days)

# # Задание 7
# goods = []
# features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
# analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
# num = 0
# feature_ = None
# control = None
# while True:
#     control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
#     if control == 'Q':
#         break
#     num += 1
#     if control == 'A':
#         print(f'\n Current analytics \n {"-" * 30}')
#         for key, value in analytics.items():
#             print(f'{key[:25]:>30}: {value}')
#             print("-" * 30)
#     for f in features.keys():
#         feature_ = input(f'Input feature "{f}"')
#         features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
#         analytics[f].append(features[f])
#     goods.append((num, features))







