s, t = map(int, input().split())
if (s > 0 and t > 0) or (s < 0 and t < 0):
    print(abs(s-t))
else:
    print(abs(s-t)-1)