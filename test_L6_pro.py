# Придумайте 2 теста к грязной функции. Примером грязной функции является функция F из задания 4.
import random
names = ('Даниил, Илья, Макар, Никон, Павел, Порфирий, Юлиан, Мария, Михаил, Николай, Роман, Федор, Феодосий, Анна, Василий, Виктор, Владимир, Кузьма, Лев, Архип')
list_20 = names.split(sep = ', ')
list_n = []

n = 100
def f(n):
    for i in range(n):
        list_n.append(random.choice(list_20))
    return list_n

# Протестируем то, что можно измерить - длину списка:
def test_1_f():
    assert len(list_n) == n

a = f(n)
list_n = []
b = f(n)
print(a)
print(b)

# Протестируем то, что нельзя измерить - работу модуля random:
def test_2_f():
    assert a != b
