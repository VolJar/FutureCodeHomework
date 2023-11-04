usr_input = input()
VCS = 1
for i in range(len(usr_input)):
    if VCS == 1 and usr_input[i].isalpha():
        usr_input = usr_input[:i] + usr_input[i].upper() + usr_input[i + 1:]
        VCS = 0
        continue
    if usr_input[i] in {".", "?", "!"}:
        VCS = 1
print(usr_input)
