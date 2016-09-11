a = list(input())
b = list(input())
c = list(input())
current = "a"
while True:
    if current == "a":
        if len(a) == 0:
            print("A")
            break
        else:
            current = a.pop(0)
    elif current == "b":
        if len(b) == 0:
            print("B")
            break
        else:
            current = b.pop(0)
    else:
        if len(c) == 0:
            print("C")
            break
        else:
            current = c.pop(0)
