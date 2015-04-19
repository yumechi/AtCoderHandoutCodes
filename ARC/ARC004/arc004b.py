N = int(input())
table = [int(input()) for _ in range(N)]
sumtable = sum(table)
print(sumtable)
maxlength = max(table)
if (sumtable - maxlength) > maxlength:
    print(0)
else:
    print(maxlength - (sumtable - maxlength))