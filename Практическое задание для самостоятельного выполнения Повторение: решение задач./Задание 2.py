ans = []


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


n_1 = int(input())
for i in range(1, n_1 + 1):
    if is_prime(i):
        ans.append(i)

print(ans)
