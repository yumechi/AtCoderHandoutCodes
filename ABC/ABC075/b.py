def solve():
    h, w = map(int, input().split())
    al = [list(input()) for _ in range(h)]
    ans = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if al[i][j] == "#":
                ans[i][j] = "#"
                continue
            cnt = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k == 0 and l == 0:
                        continue
                    if 0 <= i+k < h and 0 <= j+l < w:
                        if al[i+k][j+l] == "#":
                            cnt += 1
            ans[i][j] = str(cnt)
    for line in ans:
        print("".join(line))


if __name__=="__main__":
    solve()
