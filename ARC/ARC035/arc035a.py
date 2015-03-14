s = input()
str = s + s
a = True
i= 0
length = len(str) - 1
 
while i <= length:
    if str[i] == str[length] or str[i] == "*" or str[length] == "*":
        i += 1
        length -= 1
    else:
        a = False
        break
 
print("YES" if a else "NO")