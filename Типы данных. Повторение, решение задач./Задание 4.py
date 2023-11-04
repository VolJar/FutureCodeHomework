mat = set(input().split())
geo = set(input().split())
tri = set(input().split())
ans = []
temp = mat & geo & tri
if temp == set():
    print("Все три задачи никто не решил")
else:
    ans = list(temp)
    sorted(ans)
    for i in range(len(temp)):
        print(ans[i], end=' ')
