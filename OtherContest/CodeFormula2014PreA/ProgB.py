def replacer(li, ch):
    for elem in li:
        for i in range(4):
            table[i] = table[i].replace(str(elem), ch)
 
table = ["7 8 9 0", " 4 5 6 ", "  2 3  ", "   1   "]
a, b = map(int, input().split())
 
replacer(map(int, input().split()), ".")
replacer(map(int, input().split()), "o")
replacer(list(range(0, 10)), "x")
 
for i in range(4):
    print(table[i])