l, h = map(int, input().split())
for i in range(int(input())):
    a = int(input())
    if a < l:
        print(l - a)
    elif h < a:
        print(-1)
    else:
        print(0)
