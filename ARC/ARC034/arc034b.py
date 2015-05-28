ran = 9 * 18
N = int(input())
low = (N - ran - 1) if N > (ran + 1) else 1
res = []
for i in range(low, N):
    if i + sum(list(map(int, str(i)))) == N:
    	res.append(i)
 
print(len(res))
for r in res:
    print(r)