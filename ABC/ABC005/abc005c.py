T = int(input())
N = int(input())
tl = list(map(int, input().split()))
Q = int(input())
bl = list(map(int, input().split()))

if N < Q:
    print("no")
else:
    while len(tl) != 0 and len(bl) != 0:
        if tl[0] <= bl[0] <= tl[0] + T:
            tl.pop(0)
            bl.pop(0)
        else:
            tl.pop(0)
    print("yes" if len(bl) == 0 else "no")