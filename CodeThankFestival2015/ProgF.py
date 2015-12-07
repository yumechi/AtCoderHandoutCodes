N = int(input())
br = N-1
root = 0
for _ in range(N-1):
    s, t = map(lambda x: int(x)-1, input().split())
    if s == 0 or t == 0:
        root += 1
if root <= 1:
    print("A")
    exit(0)
else:
    if root % 2 == 1:
        print("A" if (br - root) % 2 == 0 else "B")
    else:
        print("A" if (br - root) % 2 == 1 else "B")
