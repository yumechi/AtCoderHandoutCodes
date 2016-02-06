deep = 0
s = input()
if s == "{}":
    print("dict")
    exit(0)

for c in s:
    if c == "{":
        deep += 1
    elif c == "}":
        deep -= 1
    elif c == ":" and deep == 1:
        print("dict")
        break
else:
    print("set")
