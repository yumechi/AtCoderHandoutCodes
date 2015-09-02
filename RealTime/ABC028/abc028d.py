n,k = map(int, input().split())
upi = 1 + (n - 1) * 3 + ((k - 1) * (n - k)) * 6
print(upi / (n ** 3))
