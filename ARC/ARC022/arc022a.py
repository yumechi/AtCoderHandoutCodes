s = input()
s = s.upper()
if "I" in s:
    s = s[s.find("I"):]
    if "C" in s:
        s = s[s.find("C"):]
        if "T" in s:
            print("YES")
            exit()
print("NO")