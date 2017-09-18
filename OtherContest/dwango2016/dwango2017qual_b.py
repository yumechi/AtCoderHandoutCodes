def solve():
    s = list(input())
    s2 = s[:]
    arr = ["2", "5"]
    for i in range(len(s)):
        if s[i] == "?":
            s[i] = arr[i % 2]
    for i in range(len(s2)):
        if s2[i] == "?":
            s2[i] = arr[(i+1) % 2]

    ans, t, t2 = 0, 0, 0
    for i in range(len(s)):
        if t % 2 == 0 and s[i] == "2":
            t += 1
        elif t % 2 == 1 and s[i] == "5":
            t += 1
        else:
            if t % 2 == 1:
                t -= 1
            ans = max(t, ans)
            if s[i] == "2":
                t = 1
            else:
                t = 0

        if t2 % 2 == 0 and s2[i] == "2":
            t2 += 1
        elif t2 % 2 == 1 and s2[i] == "5":
            t2 += 1
        else:
            if t2 % 2 == 1:
                t2 -= 1
            ans = max(t2, ans)
            if s2[i] == "2":
                t2 = 1
            else:
                t2 = 0

    if t % 2 == 1:
        t -= 1
    if t2 % 2 == 1:
        t2 -= 1
    ans = max(t, t2, ans)
    print(ans)

if __name__=="__main__":
    solve()
