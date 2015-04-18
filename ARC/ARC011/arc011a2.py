m, n, N = map(int, input().split())
counter = N
while N >= m:
    N -= m - n
    counter += n
print(counter)