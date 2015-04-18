N = int(input())
slist = map(int, input().split())
num = 0
for i in slist:
    if i < 80:
        num += 80 - i
print(num)
