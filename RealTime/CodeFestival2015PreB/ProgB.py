N, M = map(int, input().split())
counter = [0 for _ in range(M+1)]
for i in map(int, input().split()):
    counter[i] += 1
imax = max(counter)
print(counter.index(imax) if imax > N // 2 else "?")
