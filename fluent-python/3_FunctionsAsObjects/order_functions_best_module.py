#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from collections import namedtuple
import order_promos
import inspect

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # the Context

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def BestPromo(order):
    """Select the best discount program"""
    promos = [func for name, func in inspect.getmembers(order_promos, inspect.isfunction)]
    return max(promo(order) for promo in promos)

if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]
    banana_cart = [ LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

    print('---------------------------------------------------------------------------')

    for item in inspect.getmembers(order_promos, inspect.isfunction):
        print(item)

    print('---------------------------------------------------------------------------')

    print(Order(joe, cart, order_promos.FidelityPromo))
    print(Order(ann, cart, order_promos.FidelityPromo))
    print(Order(joe, banana_cart, order_promos.BulkItemPromo))
    print(Order(joe, long_order, order_promos.LargeOrderPromo))
    print(Order(joe, cart, order_promos.LargeOrderPromo))

    print('---------------------------------------------------------------------------')

    print(Order(joe, long_order, BestPromo))
    print(Order(joe, banana_cart, BestPromo))
    print(Order(ann, cart, BestPromo))

    print('---------------------------------------------------------------------------')

