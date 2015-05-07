name = "kogakubu10gokan"
n, q = map(int, input().split())
for _ in range(n):
    s = input().split()
    if int(s[0]) <= q:
        name = s[1]
    else:
        break
print(name)