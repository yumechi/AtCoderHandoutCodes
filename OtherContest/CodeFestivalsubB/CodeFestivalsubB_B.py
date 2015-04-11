# from my smartphone
N, K = map(int, input().split())
sum = res = 0
while sum < K:
    sum += int(input())
    res += 1
print(res)