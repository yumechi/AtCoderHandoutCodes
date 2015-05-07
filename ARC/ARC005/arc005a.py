N = int(input())
slist = input().split()
counter = 0
for i in range(N):
    if i == N - 1:
        templist = list(slist[i])
        slist[i] = "".join(templist[:len(slist[i]) - 1])
    if slist[i] == "takahashikun" or slist[i] == "Takahashikun" or slist[i] == "TAKAHASHIKUN":
        counter += 1
print(counter)