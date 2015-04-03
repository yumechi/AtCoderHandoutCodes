s = input()
while len(s) > 0:
    if s.endswith("ch"):
        s = s[:len(s) - 2]
    elif s.endswith("o"):
        s = s[:len(s) - 1]
    elif s.endswith("k"):
        s = s[:len(s) - 1]
    elif s.endswith("u"):
        s = s[:len(s) - 1]
    else:
        break

print("YES" if len(s) == 0 else "NO")