user_input = input().split()
n = int(user_input.pop(-1))  # Последнее число всегда является n - степень
print([int(i) ** n for i in user_input])
