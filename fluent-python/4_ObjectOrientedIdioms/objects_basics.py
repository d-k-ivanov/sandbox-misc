#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Gizmo:
    def __init__(self):
        print('Gizmo id is %d' % id(self))


if __name__=='__main__':
    print('-' * 100)

    # Variables not a boxes
    a = [1, 2, 3]
    b = a
    print(b)
    a.append(4)
    print(b)

    print('-' * 100)

    x = Gizmo()
    try:
        y = Gizmo() * 10
    except TypeError:
        print('TypeError: unsupported operand type(s) for *: "Gizmo" and "int"')
    print(dir()) # showd that variable 'y' not defined

    print('-' * 100)

    charles = {'name': 'Chaeles L. Dodgson', 'born': 1832}
    lewis = charles
    print(lewis is charles)
    print(id(charles), id(lewis))
    lewis['balance'] = 950
    print(charles)

    alex = {'name': 'Chaeles L. Dodgson', 'born': 1832, 'balance': 950}
    print(alex == charles)
    print(alex is not charles)

    print('-' * 100)

    t1 = (1, 2, [30, 40])
    t2 = (1, 2, [30, 40])
    print(t1 == t2)
    print(id(t1), id(t2))
    print(id(t1[0]), id(t1[1]), id(t1[2]), id(t1[-1]))
    print(id(t1[-1]))
    t1[-1].append(50)
    print(id(t1[-1]))
    print(t1 == t2)

    print('-' * 100)

    l1 = [3, [55, 44], (7, 8, 9)]
    l2 = list(l1)
    l3 = [3, [55, 44], (7, 8, 9)]
    print(l1)
    print(l2)
    print(l2 == l1)
    print(l2 is l1)
    print(l2[1] == l1[1])
    print(l2[1] is l1[1])

    print('-' * 100)

    for item in l1:
        print('{0} -> {1}'.format(item, str(id(item))))
    for item in l2:
        print('{0} -> {1}'.format(item, str(id(item))))
    for item in l3:
        print('{0} -> {1}'.format(item, str(id(item))))

    print('-' * 100)

    l1 = [3, [66, 55, 44], (7, 8, 9)]
    l2 = list(l1)
    l1.append(100)
    l1[1].remove(55)
    print(l1)
    print(l2)
    l2[1] += [33, 22]
    l2[2] += (10, 11)
    print(l1)
    print(l2)

    print('-' * 100)
