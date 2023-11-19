def NOD(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


a = int(input())
b = int(input())

print((a * b) // NOD(a, b))
