n = int(input())
if n > 1000:
    exit(0)
res = 0
for i in range(1, n+1):
    if "1" in str(i):
        res += str(i).count("1")
print(res)
