#!/usr/bin/env python3

# for (items iteration)
items = ['cat', 'hamster', 'chihuahua', 'owl']
for item in items:
    print("I have a {0}".format(item))

# for in range
for i in range(0, 10, 3):
    print(i)

# while loop
x = 10
while x > 0:
    print (x)
    x = x - 1

# array comprehensions
batch1 = [1, 2, 3, 'dog', 'chinchilla', 'cat']
batch2 = [6, 'chihuahua', 'chitah', 'wale']

pets = [pet for pet in batch1 if isinstance(pet, str)]
pets = pets + [pet for pet in batch2 if isinstance(pet, str)]
print (pets)

# array comprehensions
sales = [3.14, 7.99, 10.99]
sales_with_tax = [sale * 1.07 for sale in sales]
print (sales_with_tax)

val = 3
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

gt_than_3 = [
    number
    for number in arr
        if number > val
]

print (gt_than_3)
