#!/usr/bin/env python
# -*- coding: utf-8 -*-

# You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        l = self
        s = ""
        while l:
            s += f"{l.val} "
            l = l.next
        return s

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        result = summa = ListNode((l1.val + l2.val + c) % 10)
        # print(f"{l1.val} + {l2.val} + {c} = {l1.val + l2.val + c}")
        c = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next

        while (l1 or l2):
            if l1:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            # print(f"{a} + {b} + {c} = {a + b + c}")
            summa.next = ListNode((a + b + c) % 10)
            c = (a + b) // 10
            summa = summa.next
        else:
            if c > 0:
                summa.next = ListNode((c))
        return result


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)

while result:
    print(f"{result.val}", end = ' ') # 7 0 8
    result = result.next
print()

l1 = tmp1 = ListNode(2)
l2 = tmp2 = ListNode(5)
from random import randrange
for i in range(10):
    tmp1.next = ListNode(randrange(9))
    tmp2.next = ListNode(randrange(9))
    tmp1 = tmp1.next
    tmp2 = tmp2.next

# print(f"L1: {l1}")
# print(f"L2: {l2}")
print(l1)
print(l2)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(f"{result.val}", end = ' ')
    result = result.next
print()
