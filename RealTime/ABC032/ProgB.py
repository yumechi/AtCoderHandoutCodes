s = input()
n = int(input())

slen = len(s)
res = set([])
for i in range(slen-n+1):
    res.add(s[i:i+n])
print(len(res))
