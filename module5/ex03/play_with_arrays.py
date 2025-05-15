#!/usr/bin/env python3
array = [2, 8, 9, 48, 8, 22, -12, 2]
print(array)
for i in array:
    array_plus_2 = map (lambda i: i + 2, array)
    new_array = []
    for n in array_plus_2:
        if n > 5:
            new_array.append(n)
            new_set = set(new_array)
print(new_set)