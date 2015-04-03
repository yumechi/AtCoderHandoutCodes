A, B, C = map(int, input().split())
plusflag = (C == A + B)
minusflag = (C == A - B)
if plusflag and minusflag:
    print("?")
elif plusflag and not minusflag:
    print("+")
elif not plusflag and minusflag:
    print("-")
else:
    print("!")