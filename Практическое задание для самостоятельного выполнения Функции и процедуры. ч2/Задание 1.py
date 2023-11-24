l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
if len(l1) != len(l2):
    if len(l1) > len(l2):
        while len(l2) != len(l1):
            l2.append(0)
    if len(l2) > len(l1):
        while len(l1) != len(l2):
            l1.append(0)
print(list(map(lambda x, y: x + y, l1, l2)))
