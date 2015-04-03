n = int(input())
print("%02d:%02d:%02d" % (n // 3600,  (n % 3600) // 60, n % 60))