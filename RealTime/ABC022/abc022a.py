N, S, T = map(int, input().split())
days = weight = 0
for _ in range(N):
    weight += int(input())
    if S <= weight <= T:
        days += 1
print(days)