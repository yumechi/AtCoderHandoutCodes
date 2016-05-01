def solve():
    n = input()
    al = []
    for c in n:
        if c.isdigit():
            al.append(c)
    print(int("".join([str(i) for i in al])))

def solve2():
    import re
    print(re.sub(r'[a-zA-Z]', '', input()))

if __name__=="__main__":
    solve2()