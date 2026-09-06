#map() is used when you want to perform the same operation on every item in a collection.
 # syntax map (function , iterable)

numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number * 2)

print(result)

result = map(lambda x: x * 2, numbers)

print(list(result))


# filter()
# syntax filter (function , iterable)
# we use filter when we only need the values that satisfy our given condition

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))


# reduce()
# syntax reduce(function , iterable)

from functools import reduce

result = reduce(lambda x, y: x + y, numbers)

print(result)