ans = 0
for i in range(int(input())):
  a, b = map(int, input().split())
  ans += b + 1 - a
print(ans)
