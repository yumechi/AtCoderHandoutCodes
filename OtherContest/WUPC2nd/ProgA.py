n, k = map(int, input().split())
print(sum([i ** 2 for i in range(n + 1)]) % k)