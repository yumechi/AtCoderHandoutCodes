dinnerset = set()
N = int(input())
for _ in range(0, N):
               dinnerset.add(int(input()))
dinnerset.remove(max(dinnerset))
print(max(dinnerset))