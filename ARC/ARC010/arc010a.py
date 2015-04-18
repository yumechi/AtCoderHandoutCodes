N, M, A, B = map(int, input().split())
for i in range(M):
    if N <= A:
        N += B
    t = int(input())
    N -= t
    if N < 0:
        print(i + 1)
        break
else:
    print("complete")