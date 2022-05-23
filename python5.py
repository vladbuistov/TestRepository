# sug1 = [sym.lower() for sym in input() if sym != " " and sym not in ".,!?:;-"]
# sug2 = [sym.lower() for sym in input() if sym != " " and sym not in ".,!?:;-"]
# print("YES" if sorted(sug1) == sorted(sug2) else "NO")

# n = int(input())
# list_countries = [input().split() for i in range(n)]
# countries = {country[0]: country[1:] for country in list_countries}
#
# m = int(input())
# cities = [input() for i in range(m)]
#
# for city in cities:
#     for key, value in countries.items():
#         if city in value:
#             print(key)

# n = int(input())
# list_phones = [input().split() for i in range(n)]
# phones = {phone[0]: phone[1].lower() for phone in list_phones}
#
# m = int(input())
# names = [input().lower() for i in range(m)]
#
# for name in names:
#     if name not in phones.values():
#         print("абонент не найден")
#     else:
#         for key, value in phones.items():
#             if name == value:
#                 print(key, end=" ")
#     print()

# Множества

# Важно знать:
# все элементы множества различны (уникальны), два элемента не могут иметь одинаковое значение;
# myset1 = {2, 2, 3, 3, 4, 4}
# print(myset1)
#
# # множества неупорядочены, то есть элементы не хранятся в каком-то определенном порядке;
# myset2 = {4, 1, 9, -5, 0, 5, 3}
# print(myset2)
#
# # элементы множества должны относиться к неизменяемым типам данных;
# # myset3 = {1, 2, [3, 4], 5, 6}  # вернет ошибку
# # myset4 = {1, 2, {3, 4}, 5, 6}  # вернет ошибку
# myset5 = {1, 2, (3, 4), 5, 6}
# print(myset5)
#
# # хранящиеся в множестве элементы могут иметь разные типы данных.
# myset6 = {1, 2, (3, 4), "5", 6}
# print(myset6)
#
# # Создание пустого множества
# myset = {}  # создается словарь
# print(type(myset))
#
# myset = set()  # пустое множество
# print(type(myset))
#
# # Функция set()
#
# myset1 = set(range(10))
# myset2 = set([1, 2, 3, 4, 5])
# myset3 = set('abcd')
# myset4 = set((10, 20, 30, 40, 50))
#
# print(myset1)
# print(myset2)
# print(myset3)
# print(myset4)

# Основы работы с множествами

# Функция len()

# myset1 = {2, 2, 4, 6, 6}
# myset2 = set([1, 2, 2, 3, 3, 4, 4, 5, 5])
# myset3 = set('aaaaabbbbccccddd')
#
# print(len(myset1))
# print(len(myset2))
# print(len(myset3))
#
# # Функции sum(), min(), max()
#
# numbers = {2, 2, 4, 6, 6}
# print('Сумма всех элементов множества =', sum(numbers))
# print('Минимальный элемент =', min(numbers))
# print('Максимальный элемент =', max(numbers))
#
# # Оператор принадлежности in
#
# numbers = {2, 4, 6, 8, 10}
#
# if 2 in numbers:
#     print('Множество numbers содержит число 2')
# else:
#     print('Множество numbers не содержит число 2')


# 1. Напишите программу, которая выведет сумму квадратов элементов множества numbers
# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# list_numbers = [i**2 for i in numbers]
# print(sum(list_numbers))
#
# summa = 0
# for i in numbers:
#     summa += i**2
# print(summa)

#
# 2. Напишите программу, которая выведет элементы множества fruits, каждый на отдельной строке,
# отсортированные по убыванию (в обратном лексикографическом порядке).
# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# for fruit in sorted(fruits, reverse=True):
#     print(fruit)

# print(*sorted(fruits, reverse=True), sep="\n")
#
# 3. Напишите программу, которая определяет количество различных символов в строке. Строка вводится с клавиатуры.
#
# Пример ввода 1:
# 12345678910
# Пример вывода 1:
# 10
#
# Пример ввода 2:
# ab bc
# Пример вывода 2:
# 4

# print(len(set(input())))

# 4. На вход программе подается строка, состоящая из цифр.
# Необходимо определить, верно ли, что в ее записи ни одна из цифр не повторяется?
#
# Пример ввода 1:
# 1093482
# Пример вывода 1:
# YES
#
# Пример ввода 2:
# 10000000
# Пример вывода 2:
# NO

# c = input()
# if len(set(c)) == len(c):
#     print("YES")
# else:
#     print("NO")

# 5. На вход программе подаются две строки, состоящие из цифр.
# Необходимо определить, верно ли, что в записи этих двух строк используются все десять цифр?
#
# Пример ввода 1:
# 12387
# 94230
# Пример вывода 1:
# NO
#
# Пример ввода 2:
# 1930
# 2465748
# Пример вывода 2:
# YES

# if len(set(input() + input())) == 10:
#     print("YES")
# else:
#     print("NO")

# 6. На вход программе подаются две строки, состоящие из цифр.
# Необходимо определить, верно ли, что для записи этих строк были использованы одинаковые наборы цифр?
#
# Пример ввода 1:
# 0943
# 9304
# Пример вывода 1:
# YES
#
# Пример ввода 2:
# 1
# 2
# Пример вывода 2:
# NO

# if set(input()) == set(input()):
#     print("YES")
# else:
#     print("NO")

# 7. На вход программе подается строка, состоящая из трех слов.
# Верно ли, что для записи всех трех слов был использован один и тот же набор букв?
#
# Пример ввода 1:
# автор товар отвар
# Пример вывода 1:
# YES
#
# Пример ввода 2:
# шарада баллада услада
# Пример вывода 2:
# NO

# s = input().split()
# if set(s[0]) == set(s[1]) == set(s[2]):
#     print("YES")
# else:
#     print("NO")

# Методы множеств

# Метод add()

# numbers = {1, 1, 2, 3, 5, 8, 3}  # создаем множество
#
# numbers.add(21)  # добавляем число 21 в множество
# numbers.add(34)  # добавляем число 34 в множество
#
# print(numbers)

# Метод remove()

# numbers = {1, 2, 3, 4, 5}
#
# numbers.remove(3)
# print(numbers)

# numbers = {1, 2, 3, 4, 5}
#
# numbers.remove(10)  # вызовет ошибку
# print(numbers)

# Метод discard()

# numbers = {1, 2, 3, 4, 5}
#
# numbers.discard(3)
# print(numbers)

# numbers = {1, 2, 3, 4, 5}
#
# numbers.discard(10)
# print(numbers)

# Метод pop()

# numbers = {1, 2, 3, 4, 5}
#
# print('до удаления:', numbers)
# num = numbers.pop()                 # удаляет случайный элемент множества, возвращая его
# print('удалённый элемент:', num)
# print('после удаления:', numbers)


# Операции над множествами

# Объединение множеств: метод union()
# Объединение множеств это множество, состоящее из элементов,
# принадлежащих хотя бы одному из объединяемых множеств.

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1.union(myset2)
# print(myset3)

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1 | myset2
# print(myset3)

# Пересечение множеств: метод intersection()
# Пересечение множеств это множество, состоящее из элементов,
# принадлежащих одновременно каждому из пересекающихся множеств.

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1.intersection(myset2)
# print(myset3)

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1 & myset2
# print(myset3)

# Разность множеств: метод difference()
# Разность множеств это множество, в которое входят все элементы первого множества,
# не входящие во второе множество.

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1.difference(myset2)
# print(myset3)

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1 - myset2
# print(myset3)

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset2 - myset1
# print(myset3)

# Симметрическая разность: метод symmetric_difference()
# Симметрическая разность множеств это множество, включающее все элементы исходных множеств,
# не принадлежащие одновременно обоим исходным множествам.

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1.symmetric_difference(myset2)
# print(myset3)

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1 ^ myset2
# print(myset3)

# 1. На вход программе подаются два числа.
# Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.
#
# Пример ввода 1:
# 114
# 223
# Пример вывода 1:
# NO
#
# Пример ввода 2:
# 1523
# 3678
# Пример вывода 2:
# YES
#
# Пример ввода 3:
# 5543
# 3455
# Пример вывода 3:
# YES

# ch1 = input()
# ch2 = input()
# if set(ch1).isdisjoint(ch2):
#     print("NO")
# else:
#     print("YES")

# 2. На вход программе подаются два числа. Напишите программу, которая определяет, входят ли в запись первого числа все цифры,
# содержащиеся в записи второго (независимо от повтора, то есть количества цифр) числа, или нет.
#
# Пример ввода 1:
# 123456789
# 657
# Пример вывода 1:
# YES
#
# Пример ввода 2:
# 1254
# 1243
# Пример вывода 2:
# NO
#
# Пример ввода 3:
# 12345678
# 999
# Пример вывода 3:
# NO

# ch1 = input()
# ch2 = input()
# if set(ch1).issuperset(ch2):
#     print("YES")
# else:
#     print("NO")

# 3. Даны оценки по информатике трех учеников по 10-балльной шкале.
# Напишите программу, которая выводит множество оценок, которые есть и у первого и у второго учеников, но которых нет у третьего ученика.
#
# Пример ввода 1:
# 2 9 3 4 6 10
# 2 3 4 5 2 10
# 2 3 4 5 3 9
# Пример вывода 1:
# 10
#
# Пример ввода 2:
# 1 5 4 2 5 6 6 2 3 3 5 2
# 2 3 5 1 2 1 2 6 7 1 1 6
# 1 4 6 9 8 7 0 9 0 9 8 10
# Пример вывода 2:
# 5 3 2

# set1 = set(input().split())
# set2 = set(input().split())
# set3 = set(input().split())
#
# print(*set1.intersection(set2).difference(set3))

# 4. Даны оценки по физике трех учеников по 10-балльной шкале.
# Напишите программу, которая выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика.
#
# Пример ввода 1:
# 1 5 4 2 5 6 6 2 3 3 5 2
# 2 3 5 1 2 1 2 6 7 1 1 6
# 1 4 6 9 8 7 0 9 0 9 8 10
# Пример вывода 1:
# 10 9 8 0
#
# Пример ввода 2:
# 2 9 2 4 6 10
# 2 2 4 5 2 10
# 2 3 4 5 3 9
# Пример вывода 2:
# 3

# set1 = set(input().split())
# set2 = set(input().split())
# set3 = set(input().split())
#
# print(*(set3 - set2 - set1))

# 5. Даны оценки по биологии трех учеников по 10-балльной шкале.
# Напишите программу, которая выводит множество оценок, не встречающихся ни у одного из трех учеников.
#
# Пример ввода 1:
# 2 9 3 4 6 10
# 2 3 4 5 2 10
# 2 3 4 5 3 9
# Пример вывода 1:
# 0 1 7 8
#
# Пример ввода 2:
# 1 5 4 2 5 6 6 2 3 3 5 2
# 2 3 5 1 2 1 2 6 7 1 1 6
# 1 4 6 8 8 7 0 6 0 3 8 1
# Пример вывода 2:
# 9 10

# set1 = set(input().split())
# set2 = set(input().split())
# set3 = set(input().split())
#
# set_all = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '0'}
# print(*(set_all - set1 - set2 - set3))

# Генераторы множеств

# digits = set()
# for i in input():
#     digits.add(int(i))
# print(digits)

# {выражение for переменная in последовательность}

# digits = {int(i) for i in input()}
# print(digits)
#
# squares = {i**2 for i in range(10)}
# print(squares)
#
# chars = {sym for sym in "abcdef"}
# print(chars)
#
# digits = {int(i) for i in "abcd12f78ghk332" if i.isdigit()}
# print(digits)

# Замороженные множества (frozenset)

# set1 = frozenset({1, 2, 3})
# set2 = frozenset([1, 2, 3, 4, 5, 6, 7, 8, 9])
# set3 = frozenset("abcdef")
#
# print(set1, set2, set3)


# 1. Используя генератор множеств, напишите программу, чтобы получить множество, содержащее уникальные значения списка items.
# Результат вывести на одной строке, в упорядоченном виде, разделяя элементы одним символом пробела.
#
# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
#
# Примечание 1. Обратите внимание, некоторые элементы списка – числа, а некоторые – строки, при этом строки необходимо трактовать как числа.
#
# Примечание 2. Чтобы вывести элементы множества в упорядоченном виде используйте следующий код:

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# myset = {int(i) for i in items}
# print(*sorted(myset))
#
# 2. Используя генератор множеств, напишите программу, чтобы получить множество, содержащее первую букву каждого слова (в нижнем регистре) списка words.
# Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним символом пробела.
#
# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# myset = {word[0].lower() for word in words}
# print(*sorted(myset))

# 3. Используя генератор множеств, напишите программу, чтобы получить множество, содержащее уникальные слова (в нижнем регистре) строки sentence.
# Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним символом пробела.
#
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# myset = {word.strip(".,:;()?!") for word in sentence.split()}
# print(*sorted(myset))

# 4. Используя генератор множеств, напишите программу, чтобы получить множество, содержащее уникальные слова строки sentence длиною меньше 4 символов. Результат вывести на одной строке (в нижнем регистре) в алфавитном порядке, разделяя элементы одним символом пробела.
#
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# myset = {word.strip(".,:;()?!") for word in sentence.split()}
# new_myset = {word for word in myset if len(word) < 4}
# print(*sorted(new_myset))

# 5. Используя генератор множеств, напишите програму, чтобы выбрать из списка files уникальные имена файлов c расширением .png, независимо от регистра имен и расширений.
# Имена файлов вывести вместе с расширением, все на одной строке, в нижнем регистре, в алфавитном порядке через пробел.
#
# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
# myset = {file.lower() for file in files if file.lower().endswith(".png")}
# print(*sorted(myset))


# Примечание. Если бы список files содержал следующие имена файлов:
# files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
# то ответом был бы:
# apple.png python.png zebra.png


# # Функции
#
# # Объявление функции
# # def название_функции():
# #     блок кода
#
# def print_hello():
#     print("Hello, world")
#     print("How are you?")
#
# # вызов функции
# print_hello()
# print_hello()
# print_hello()

# 1. Звездный прямоугольник
# Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10 в соответствии с образцом:
#
# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********

# def draw_box():
#     print("*" * 10)
#     for i in range(12):
#         print("*" + " " * 8 + "*")
#         # print("*        *")
#     print("*" * 10)
#
# draw_box()

# Примечание. Для вывода прямоугольника используйте цикл for.
#
# 2. Звездный треугольник
# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10 в соответствии с образцом:
#
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
#
# Примечание. Для вывода треугольника используйте цикл for.

# def draw_triangle():
#     for i in range(1, 11):
#         print("*" * i)
#
#
# draw_triangle()

# Функции с параметрами

# def draw_box(height, width):
#     for i in range(height):
#         print("*" * width)
#
#
# h, w = int(input()), int(input())
# draw_box(h, w)

# def summa(n1, n2):
#     print(n1 + n2)
#
# num1, num2 = int(input()), int(input())
# summa(num1, num2)

# 1. Звездный треугольник
# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
#
# а затем выводит его.
#
# Примечание. Гарантируется, что основание треугольника – нечетное число.
#
# Пример ввода 1:
# *
# 9
#
# Пример вывода 1:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
#
# Пример ввода 2:
# +
# 5
#
# Пример вывода 2:
# +
# ++
# +++
# ++
# +

# def draw_triangle(fill, base):
#     for i in range(1, base // 2 + 2):
#         print(fill * i)
#     for i in range(base // 2, 0, -1):
#         print(fill * i)
#
#
# f, b = input(), int(input())
# draw_triangle(f, b)

# 2. ФИО
# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
#
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.
#
# Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
#
# Пример ввода 1:
# Александр
# Пушкин
# Сергеевич
#
# Пример вывода 1:
# ПАС
#
# Пример ввода 2:
# тимур
# Гуев
# ахсарбекович
#
# Пример вывода 2:
# ГТА


# def print_fio(name, surname, patronymic):
#     print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep="")
#
#
# n, s, p = input(), input(), input()
# print_fio(n, s, p)


# 3. Сумма цифр
# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
#
# Пример ввода 1:
# 12345
#
# Пример вывода 1:
# 15
#
# Пример ввода 2:
# 12
#
# Пример вывода 2:
# 3


# def print_digit_sum(number):
#     print(sum([int(i) for i in number]))
#
#
# n = input()
# print_digit_sum(n)


# Локальные и глобальные переменные

# def print_texas():
#     birds = 3000
#     print('В Техасе обитает', birds, 'птиц.')
#
#
# def print_california():
#     global birds
#     birds = 9000
#     print('В Калифорнии обитает', birds, 'птиц.')
#
#
# birds = 5000
# print(birds)
# print_texas()
# print_california()
# print(birds)

# Функции с возвратом значения

# def название_функции():
#     блок кода
#     return выражение

# def summa(a, b):
#     return a + b
#
#
# s = summa(7, 10)
# print(s)


# def print_digit(num):
#     if num > 0:
#         return 1
#     elif num == 0:
#         return 0
#     else:
#         return -1
#
#
# n = int(input())
# print(print_digit(n))

# 1. Конвертер километров
# Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях.
# Формула для преобразования: мили = километры * 0.6214.
#
# Примечание. Следующий программный код:
# print(convert_to_miles(1))
# print(convert_to_miles(5))
# print(convert_to_miles(10))
# должен выводить:
# 0.6214
# 3.107
# 6.214

# def convert_to_miles(km):
#     return round(km * 0.6214, 3)
#
#
# km = int(input())
# print(convert_to_miles(km))

# 2. Количество дней
# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.
#
# Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.
# Примечание 2. Считайте, что год является невисокосным.
# Примечание 3. Следующий программный код:
# print(get_days(1))
# print(get_days(2))
# print(get_days(9))
# должен выводить:
# 31
# 28
# 30

# def get_days(month):
#     quantities_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return quantities_days[month-1]
#
#
# print(get_days(int(input())))

# 3. Делители 1
# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.
#
# Примечание. Следующий программный код:
# print(get_factors(1))
# print(get_factors(5))
# print(get_factors(10))
# должен выводить:
# [1]
# [1, 5]
# [1, 2, 5, 10]

# def get_factors(num):
#     d = []
#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             d.append(i)
#     d.append(num)
#     return d
#
#
# print(get_factors(int(input())))


# Функции с возвратом нескольких значений

# return выражение 1, выражение 2, выражение 3

# def get_powers(num):
#     return num**2, num**3, num**4
#
#
# a, b, c = get_powers(int(input()))
# print(a)
# print(b)
# print(c)

# print(*get_powers(int(input())))

# Возвращение булевых (логических) значений

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# number = int(input())
# if is_even(number):
#     print("Это четное число")
# else:
#     print("Это нечетное число")

# def is_invalid(num):
#     if number != 100 and number != 200 and number != 300:
#         return True
#     else:
#         return False
#
#
# number = int(input())
#
# while is_invalid(number):
#     print("Допустимыми значениями являются 100, 200 и 300")
#     number = int(input())


# 5. Площадь и длина
# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности
# и возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.
#
# Примечание 1. Длина окружности и площадь круга радиуса r вычисляются по формулам: С = 2πr, S = πr^2.
#
# Примечание 2. Для числа π используйте глобальную константу из модуля math.
#
# Примечание 3. Следующий программный код:
# print(get_circle(1))
# print(get_circle(1.5))
# должен выводить:
# 6.283185307179586
# 3.141592653589793
# 9.42477796076938
# 7.0685834705770345

# from math import pi
#
# print(pi)
#
# def get_circle(radius):
#     return 2*pi*radius, pi*radius**2
#
#
# r = float(input())
# print(*get_circle(r))


# from tkinter import *
#
#
# def add_digit(digit):
#     value = calc.get()
#     if value[0] == "0":
#         value = ""
#     calc.delete(0, END)
#     calc.insert(0, value+digit)
#
#
# def add_operation(operation):
#     value = calc.get()
#     if value[-1] in "+-*/":
#         value = value[:-1]
#     calc.delete(0, END)
#     calc.insert(0, value+operation)
#
# def calculate():
#     value = calc.get()
#     calc.delete(0, END)
#     calc.insert(0, eval(value))
#
# def clear():
#     calc.delete(0, END)
#     calc.insert(0, "0")
#
#
# def make_digit_button(digit):
#     return Button(win, text=digit, font=("Arial, 13"), command=lambda: add_digit(digit))
#
#
# def make_operation_button(operation):
#     return Button(win, text=operation, font=("Arial, 13"), command=lambda: add_operation(operation))
#
#
# def make_calc_button():
#     return Button(win, text="=", font=("Arial, 13"), command=calculate)
#
#
# def make_clear_button():
#     return Button(win, text="C", font=("Arial, 13"), command=clear)
#
#
# win = Tk()
#
# win.title("Калькулятор")
# win.geometry("240x270")
# win.resizable(False, False)
#
# calc = Entry(win, font=("Arial, 13"), justify=RIGHT)
# calc.insert(0, "0")
# calc.grid(row=0, column=0, columnspan=4, sticky="we")
#
# make_digit_button("7").grid(row=1, column=0, sticky='wens', padx=5, pady=5)
# make_digit_button("8").grid(row=1, column=1, sticky='wens', padx=5, pady=5)
# make_digit_button("9").grid(row=1, column=2, sticky='wens', padx=5, pady=5)
# make_digit_button("4").grid(row=2, column=0, sticky='wens', padx=5, pady=5)
# make_digit_button("5").grid(row=2, column=1, sticky='wens', padx=5, pady=5)
# make_digit_button("6").grid(row=2, column=2, sticky='wens', padx=5, pady=5)
# make_digit_button("1").grid(row=3, column=0, sticky='wens', padx=5, pady=5)
# make_digit_button("2").grid(row=3, column=1, sticky='wens', padx=5, pady=5)
# make_digit_button("3").grid(row=3, column=2, sticky='wens', padx=5, pady=5)
# make_digit_button("0").grid(row=4, column=1, sticky='wens', padx=5, pady=5)
#
# make_operation_button("+").grid(row=1, column=3, sticky='wens', padx=5, pady=5)
# make_operation_button("-").grid(row=2, column=3, sticky='wens', padx=5, pady=5)
# make_operation_button("*").grid(row=3, column=3, sticky='wens', padx=5, pady=5)
# make_operation_button("/").grid(row=4, column=3, sticky='wens', padx=5, pady=5)
#
# make_calc_button().grid(row=4, column=0, sticky='wens', padx=5, pady=5)
# make_clear_button().grid(row=4, column=2, sticky='wens', padx=5, pady=5)
#
# win.grid_columnconfigure(0, minsize=60)
# win.grid_columnconfigure(1, minsize=60)
# win.grid_columnconfigure(2, minsize=60)
# win.grid_columnconfigure(3, minsize=60)
#
# win.grid_rowconfigure(1, minsize=60)
# win.grid_rowconfigure(2, minsize=60)
# win.grid_rowconfigure(3, minsize=60)
# win.grid_rowconfigure(4, minsize=60)
#
# win.mainloop()


from tkinter import *
from tkinter.ttk import Combobox

# Combobox
# def show():
#     print(combo.get())
#
#
# win = Tk()
# combo = Combobox(win, values=[1, 2, 3, 4, "Text"], state='readonly')
# combo.current(1)
# combo.pack()
# btn = Button(win, text="Выбрать", command=show)
# btn.pack()
# win.mainloop()

# Radiobutton (переключатель)
# win = Tk()
#
# var = BooleanVar()
# var.set(0)
#
# r1 = Radiobutton(text="First", variable=var, value=0)
# r2 = Radiobutton(text="Second", variable=var, value=1)
#
# r1.pack()
# r2.pack()
#
# win.mainloop()

# def red_lable():
#     label['bg'] = 'red'
#
#
# def green_lable():
#     label['bg'] = 'green'
#
#
# def blue_lable():
#     label['bg'] = 'blue'
#
#
# win = Tk()
#
# var = IntVar()
# var.set(0)
#
# red = Radiobutton(text="Красный", variable=var, value=0, command=red_lable)
# green = Radiobutton(text="Зеленый", variable=var, value=1, command=green_lable)
# blue = Radiobutton(text="Синий", variable=var, value=2, command=blue_lable)
#
# label = Label(width=20, height=10)
#
# red.pack()
# green.pack()
# blue.pack()
# label.pack()
#
# win.mainloop()


# Checkbutton

# def show():
#     s1 = var1.get()
#     s2 = var2.get()
#     label['text'] = s1, s2
#
#
# win = Tk()
#
# var1 = BooleanVar()
# var2 = BooleanVar()
#
# c1 = Checkbutton(text="First", variable=var1, command=show)
# c2 = Checkbutton(text="Second", variable=var2, command=show)
# label = Label()
#
# c1.pack()
# c2.pack()
# label.pack()
#
# win.mainloop()