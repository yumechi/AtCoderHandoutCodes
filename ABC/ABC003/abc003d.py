import math

MODNUM = 10**9 + 7

def mycombi(n, r):
    upper = math.factorial(n)
    lower = math.factorial(r) * math.factorial(n - r)
    return (upper // lower) % MODNUM

R, C = map(int, input().split())
X, Y = map(int, input().split())
D, L = map(int, input().split())

tate = R - X + 1
yoko = C - Y + 1
# pattern = tate * yoko * mycombi(D + L, D)

print(tate * yoko * mycombi(D + L, D) % MODNUM)