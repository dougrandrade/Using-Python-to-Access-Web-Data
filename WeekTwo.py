# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 15:44:01 2021

@author: dougr
"""

import re
fname = input('Enter file name: ')
handle = open(fname)
numlist = list()

counts = dict()
for line in handle:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    if len(num) == 0: continue
    for i in range(len(num)):
        nums = int(num[i])
        numlist.append(nums)

print('\nThere are ', len(numlist), ' lines with numbers, with a totol sum of ', sum(numlist), '\n', sep = '')

print(sum([int(i) for i in re.findall('[0-9]+', open('regex_sum_1151151.txt').read())]))
