m, n, N = map(int, input().split())
counter = 0
unused = 0
while N > 0:
    counter += N
    unused += N - (N // m * m)
    addpencil = 0 
    while m <= unused:
        unused -= m
        addpencil += n
    N = N // m * n + addpencil
print(counter)