# -*- coding: utf-8 -*-

import random

print "Hello World"

amount = 5*6
msg = "Hello World"

print msg + str(amount)

if amount > 30:
    print "More than 30"
else:
    print "Less than 30"

rand = random.randrange(1, 50)
print rand


for x in range(1, rand+1):
    print x

while amount > 0:
    print amount
    amount -= 1

# saves resources
for x in xrange(1, rand+1):
    print x

list = ['x', 'y']
tuple = ('x', 'y')
dict = {'x': 'y', 'z': 'o'}

list.append('w')
# tuple['s'] = 1 generate error where tuple is immutable
dict['s'] = 1

print list[1]
print tuple[1]
print dict['x']

for x in list:
    print x

for x in tuple:
    print x


def printArray(arr):
    for x in dict:
        print x + ' = ' + str(dict[x])

printArray(dict)