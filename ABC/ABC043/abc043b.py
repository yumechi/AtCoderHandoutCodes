def solve():
    res = ""
    for c in input():
        if c != "B":
            res += c
        else:
            res = res[:-1] if len(res) > 0 else ""
    print(res)


if __name__=="__main__":
    solve()