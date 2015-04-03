n, X = map(int, input().split())
alist = list(map(int, input().split()))
money = 0
for goods in alist:
    t = X & 1
    X >>= 1
    if t == 1:
        money += goods
print(money)