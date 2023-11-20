import math

ans = []


def prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


n_1 = int(input())
for j in range(1, n_1 + 1):
    if prime(j):
        ans.append(j)
print(ans)
