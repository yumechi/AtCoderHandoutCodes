for _ in range(int(input())):
    s, t = map(str, input().split())
    res = ""
    for c in s:
        if c in t:
            res += c
    print("YES" if res != "" and t in res else "NO")
