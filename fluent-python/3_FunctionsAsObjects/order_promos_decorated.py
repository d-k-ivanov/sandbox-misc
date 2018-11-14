#!/usr/bin/env python
# -*- coding: utf-8 -*-

promos = []

def Promotion(promo_function):  # Decorator
    promos.append(promo_function)
    return promo_function

@Promotion
def FidelityPromo(order):  # First Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@Promotion
def BulkItemPromo(order):  # Second Concrete Strategy
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@Promotion
def LargeOrderPromo(order):  # Third Concrete Strategy
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def BestPromo(order):
    """Select the best discount program"""
    return max(promo(order) for promo in promos)
