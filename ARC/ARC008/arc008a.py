N = int(input())
print(N // 10 * 100 + N % 10 * 15 if N % 10 < 7 else (N // 10 + 1) * 100)