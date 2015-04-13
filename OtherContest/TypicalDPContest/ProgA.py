N = int(input())
ls = list(map(int, input().split()))
s = set([0])
for i in range(0, N):
    s |= set(map(lambda x: x + ls[i], list(s)))
print(len(s))