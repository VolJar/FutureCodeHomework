inpt = input()
result = []
count = 0
token = inpt.split("(")[1:]
for i in range(len(token)):
    token[i] = token[i].split(")")[0]
    result.append(token[i])
    count += 1
for i in range(count):
    print(result[i])
