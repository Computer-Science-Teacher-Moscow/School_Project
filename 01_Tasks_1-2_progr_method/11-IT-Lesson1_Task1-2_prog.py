# Решение задания 1 ЕГЭ программным способом
# Задача 01B из PDF файла
from itertools import permutations # Импорт функции (метода) permutations (перестановки без повторений) из модуля itertools

table = '1246 216 357 415 5347 6127 7356' # создаем на основе таблицы строку где у каждой подгруппы первая цифра - номер строки, последующие цифры - номера связей
graph = 'AGBC BGAE CAFD DCF EBF FEDC GBA' # на основе графа создаем строку где у каждой подгруппы первая буква - имя узловой точки, последющие буквы - имена узлов, с которыми связана первая буква

print(*'1234567') # Выводим заголовок таблицы из симфолов строки, распакованных оператором * (по умолчанию через пробел)
graph = {x[0]: set(x[1:]) for x in graph.split()} # На основе строки graph создаем через генератор словаря словарь с ключем узловой точки и значенем из множества (set()) точек, связанных с узлом

for per in permutations('ABCDEFG'): # перебираем все перестановки без повторений из названий улов, водящих в граф
    new_graph = table # на каждой итерации строим новый граф на основе таблицы
    for x,y in zip('1234567',per): # в функции zip() объединяем попарно элементы из двух итерируемых объектов и сразу распаковывыем пару в переменные x,y
        new_graph = new_graph.replace(x,y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()} # строим словарь "нового графа" на основе полученной строки new_graph
    if graph == new_graph:
        print(*per)

# Задача 04 P из PDF файла
from itertools import permutations

table = '1345 2367 31267 4156 5147 6234 7235'
graph = 'АБГВ БАДЖ ВАГЕ ГДАВ ДГЕЖБ ЕВДЖ ЖЕДБ'

print(*'1234567')
graph = {x[0]: set(x[1:]) for x in graph.split()}

for per in permutations('АБВГДЕЖ'):
    new_graph = table
    for x,y in zip('1234567',per):
        new_graph = new_graph.replace(x,y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if graph == new_graph:
        print(*per)

# Тип задания 2
# Задача 01 B
from itertools import product, permutations


def f(x, y, w, z):
    return ((w <= y) <= x) or (not z)


for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    table = ((a1, a2, 1, a3), (a4, 0, a5, a6), (a7, 1, 0, 0))
    if len(table) == len(set(table)):
        for per in permutations('wxyz'):
            if [f(**dict(zip(per, row))) for row in table] == [0, 0, 0]:
                print(*per, sep='')

# Задача 04 P
from itertools import product, permutations


def f(x, y, w, z):
    return w and ((y <= x) <= z)


for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    table = ((a1, a2, 0, 1), (0, a3, a4, 0), (0, 1, a5, 1))
    if len(set(table)) == 3:
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [1, 1, 0]:
                print(*per, sep='')
