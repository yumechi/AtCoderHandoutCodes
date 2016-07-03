a, b, k, l = map(int, input().split())
if a > l / b:
    t = k // l
    if k % l == 0:
        print(t * b)
    else:
        print(min((t + 1) * b, t * b + (k % l) * a))
else:
    print(k * a)