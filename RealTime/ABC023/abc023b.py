n = int(input())
s = input()
accessory = "b"

if s == accessory:
    print(0)
    exit(0)

for i in range(n):
    if accessory == s:
        print(i - 1)
        exit(0)
    if i % 3 == 1:
        accessory = "a" + accessory + "c"
    elif i % 3 == 2:
        accessory = "c" + accessory + "a"
    elif i > 0:
        accessory = "b" + accessory + "b"
else:
    print(-1)