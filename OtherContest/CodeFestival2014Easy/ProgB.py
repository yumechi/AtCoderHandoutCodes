n = int(input()) % 40
print(n if 1 <= n <= 20 else (40 - n + 1))