from itertools import count
from typing import Counter


list_of_numbers = []
n = int(input("Enter length of list:"))
for i in range(1, n+1):
    list_item = int(input("Enter list items:"))
    list_of_numbers.append(list_item)
print(list_of_numbers)

final_count = dict()

for k in range(1,10):
    counter = 0
    for j in list_of_numbers:
        if j % k == 0:
            counter += 1
        final_count[k] = counter

print(final_count)