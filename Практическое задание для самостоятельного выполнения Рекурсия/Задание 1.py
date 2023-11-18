def recurs_max(l1):
    if len(l1) == 0:
        return None
    if len(l1) == 1:
        return l1[0]
    else:
        if l1[0] > recurs_max(l1[1:]):
            return l1[0]
        else:
            return recurs_max(l1[1:])


print(recurs_max(list(map(int, input().split()))))
