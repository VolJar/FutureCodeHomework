l1 = list(map(int, input().split()))
print(list(filter(lambda x: x % 19 == 0 and x % 13 == 0, l1 )))
