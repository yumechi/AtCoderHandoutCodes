s = str(bin(int(input())))[2:]
print("Yes" if s == s[::-1] else "No")