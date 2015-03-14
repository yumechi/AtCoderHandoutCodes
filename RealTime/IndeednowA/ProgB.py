N = int(input())
for i in range(0, N):
    S = input()
    if len(S) != len("indeednow"):
        print("NO")
    else:
        inum = S.count("i")
        nnum = S.count("n")
        dnum = S.count("d")
        enum = S.count("e")
        onum = S.count("o")
        wnum = S.count("w")
        print("YES" if inum == onum == wnum == 1 and nnum == dnum == enum == 2 else "NO")