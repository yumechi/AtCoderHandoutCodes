li = list(map(int, input().split()))
ma, mi = max(li), min(li)
print(ma if li.count(ma) % 2 == 1 else mi)
