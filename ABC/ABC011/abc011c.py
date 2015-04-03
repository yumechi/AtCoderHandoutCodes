n = int(input())
nglist = []
for _ in range(0, 3):
    nglist.append(int(input()))

if n in nglist:
    print("NO")
    exit(0)

for i in range(0, 100):
    for j in reversed(range(1, 4)):
        if (n - j) in nglist:
            if j == 1:
                print("NO")
                exit(0)
        else:
            n -= j
            break

else:
    print("YES" if n < 1 else "NO")