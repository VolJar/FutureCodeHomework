# Раздел ввода
RC = int(input())
usr_list = []
for count in range(RC):
    temp = input()
    usr_list.append(temp)
# Раздел проверки повторений
usr_set = set(usr_list)
repeat = set()
for i in range(RC):
    for j in range(RC):
        if usr_list[i] == usr_list[j] and i != j:
            repeat.add(usr_list[i])
# Вывод
ans = len(repeat) + RC - len(usr_set)
print(ans)
