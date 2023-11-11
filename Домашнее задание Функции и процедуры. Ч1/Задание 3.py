# Функция
def maximum_number(a, b, c=None):
    if c is not None:
        return a if a > b and a > c else b if b > a and b > c else c
    else:
        return a if a > b else b


c = int(input())
if c == 2:
    print(maximum_number(int(input()), int(input())))
elif c == 3:
    print(maximum_number(int(input()), int(input()), int(input())))
else:
    print("OUT OF PROGRAM")
