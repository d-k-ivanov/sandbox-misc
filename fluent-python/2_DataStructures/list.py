#!/use/bin/env python
# -*- coding: utf-8 -*-

print('---------------------------------------------------------------------------')
l1 = list(range(10))
print(l1)

l1[2:5] = [20, 30]
print(l1)

del l1[5:7]
print(l1)

l1[3::2] = [11, 22]
print(l1)

l1[2:5] = [100]
print(l1)

print('---------------------------------------------------------------------------')

l2 = [1,2,3]
print(l2)
print(l2 * 5)

print('---------------------------------------------------------------------------')

board1 = [['_'] * 3 for i in range(3)]
print(board1)
board1[1][2] = 'X'
print(board1)

board1_1 = []
for i in range(3):
    row1 = ['_'] * 3
    board1_1.append(row1)
print(board1_1)
board1_1[1][2] = 'X'
print(board1_1)

print('---------------------------------------------------------------------------')

board2 = [['_'] * 3] * 3
print(board2)
board2[1][2] = 'X'
print(board2)

row2 = ['_'] * 3
board2_1 = []
for i in range(3):
    board2_1.append(row2)
print(board2_1)
board2_1[1][2] = 'X'
print(board2_1)

print('--------------------------- Augmented Assigment ---------------------------')

aug_l1 = [1,2,3]
print('{:10} = {:d} | {}'.format("aug_l1_id", id(aug_l1), aug_l1))
aug_l1 *= 2
print('{:10} = {:d} | {}'.format("aug_l1_id", id(aug_l1), aug_l1))

aug_t1 = (1,2,3)
print('{:10} = {:d} | {}'.format("aug_t1_id", id(aug_t1), aug_t1))
aug_t1 *= 2
print('{:10} = {:d} | {}'.format("aug_t1_id", id(aug_t1), aug_t1))

aug_t2 = (1,2,[10,20])
print('{:10} = {:d} | {:}'.format("aug_t1_id", id(aug_t2), aug_t2))
# aug_t2[2] += [30,40] # This one won't work
aug_t2[2].extend([30,40])
print('{:10} = {:d} | {}'.format("aug_t1_id", id(aug_t2), aug_t2))

print('--------------------------- List Sort -------------------------------------')

vegetables = ['tomato', 'cucumber' , 'spinach'  , 'lettuce', 'turnip', 'cabbage',
              'mallow', 'broccoli' , 'artishoke', 'pea'    , 'garlic', 'carrot' ]

print('Orig -> ' + str(vegetables))
print('Sort -> ' + str(sorted(vegetables)))
print('Sort -> ' + str(sorted(vegetables, key=len)))
print('Sort -> ' + str(sorted(vegetables, reverse=True)))
print('Orig -> ' + str(vegetables))
vegetables.sort()
print('Orig -> ' + str(vegetables))

print('---------------------------------------------------------------------------')

unsorted_list = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
print(sorted(unsorted_list, key=int))
print(sorted(unsorted_list, key=str))

print('---------------------------------------------------------------------------')
