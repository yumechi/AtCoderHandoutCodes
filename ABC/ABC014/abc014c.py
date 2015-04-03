n = int(input())
s = [0] * 1000002
for i in range(0, n):
    a, b = map(int, input().split())
    s[a] += 1
    s[b + 1] -= 1
 
for i in range(0, 1000000):
    s[i + 1] += s[i]
 
print(max(s))