#!/usr/bin/env python
# -*- coding: utf-8 -*-


def f(a,b):
    a +=  b
    return a

if __name__=='__main__':

    print('-' * 100)

    x = 1
    y = 2
    print('{0:15}: {1}'.format(str(id(x)), x))
    print('{0:15}: {1}'.format(str(id(y)), y))
    print(f(x,y))
    print('{0:15}: {1}'.format(str(id(x)), x))
    print('{0:15}: {1}'.format(str(id(y)), y))

    print('-' * 100)

    a = [1, 2]
    b = [3, 4]
    print('{0:15}: {1}'.format(str(id(a)), a))
    print('{0:15}: {1}'.format(str(id(b)), b))
    print(f(a,b))
    print('{0:15}: {1}'.format(str(id(a)), a))
    print('{0:15}: {1}'.format(str(id(b)), b))

    print('-' * 100)

    t = (10, 20)
    u = (30, 40)
    print('{0:15}: {1}'.format(str(id(t)), t))
    print('{0:15}: {1}'.format(str(id(u)), u))
    print(f(t,u))
    print('{0:15}: {1}'.format(str(id(t)), t))
    print('{0:15}: {1}'.format(str(id(u)), u))

    print('-' * 100)

    class HauntedBus:
        """A bus model haunted by ghost passengers"""

        def __init__(self, passengers=[]):
            self.passengers = passengers

        def pick(self, name):
            self.passengers.append(name)

        def drop(self, name):
            self.passengers.remove(name)

    bus1 = HauntedBus(['Alice', 'Bill'])
    print(bus1.passengers)
    bus1.pick('Charlie')
    bus1.drop('Alice')
    print(bus1.passengers)
    bus2 = HauntedBus()
    bus2.pick('Carrie')
    print(bus2.passengers)
    bus3 = HauntedBus()
    print(bus3.passengers)
    bus3.pick('Dave')
    print(bus2.passengers)
    print(bus3.passengers)
    print(bus2.passengers is bus3.passengers)
    print(bus1.passengers)

    print('-' * 100)

    print(dir(HauntedBus.__init__))
    print(HauntedBus.__init__.__defaults__)
    print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)
    print(HauntedBus.__init__.__defaults__[0] is bus3.passengers)

    print('-' * 100)

    class TwilightBus:
        """A bus model that makes passengers vanish"""

        def __init__(self, passengers=None):
            if passengers is None:
                self.passengers = []
            else:
                self.passengers = passengers

        def pick(self, name):
            self.passengers.append(name)

        def drop(self, name):
            self.passengers.remove(name)

    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
    bus_bbt = TwilightBus(basketball_team)
    bus_bbt.drop('Tina')
    bus_bbt.drop('Pat')
    print(basketball_team)

    print('-' * 100)
