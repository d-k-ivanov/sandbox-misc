#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == '__main__':
    # exec(open("1_Prologue/french_deck.py").read())
    import random
    print('----------------------------------------------------------------------')
    print(Card('7', 'diamonds'))
    print('----------------------------------------------------------------------')
    deck = FrenchDeck()
    print(len(deck))
    print('----------------------------------------------------------------------')
    print(deck[0])
    print(deck[4])
    print(deck[-1])
    print('----------------------------------------------------------------------')
    print(random.choice(deck))
    print(random.choice(deck))
    print(random.choice(deck))
    print(random.choice(deck))
    print('----------------------------------------------------------------------')
    print(deck[:3])
    print(deck[12::13])
    print('----------------------------------------------------------------------')
    for card in deck:
        print(card)
    print('----------------------------------------------------------------------')
    for card in reversed(deck):
        print(card)
    print('----------------------------------------------------------------------')


