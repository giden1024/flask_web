#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/10/28 17:50
@desc:
"""
from collections import defaultdict
from random import randrange,choice
# import curses

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

actions_dict = dict(zip(letter_codes,actions * 2))
print(actions_dict)

