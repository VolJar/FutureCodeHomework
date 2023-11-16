from functools import reduce

l1 = list(map(int, input().split()))
all_max = reduce(lambda a, b: a if (a > b) else b, l1)
print(all_max)
