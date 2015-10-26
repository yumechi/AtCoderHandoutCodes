N, M = map(int, input().split())
if N < M:
    print("NO")
    exit(0)
al = [int(x) for x in input().split()]
bl = [int(x) for x in input().split()]
al.sort(reverse=True)
bl.sort(reverse=True)
for i in range(M):
    if bl[i] > al[i]:
        print("NO")
        exit(0)
print("YES")
