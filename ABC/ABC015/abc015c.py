def dfs(num, val):
    if num == N:
        return val == 0
    for i in range(K):
        if dfs(num + 1, val ^ tlist[num][i]):
            return True
    return False


N, K = map(int, input().split())
tlist = [list(map(int, input().split())) for _ in range(N)]
print("Found" if dfs(0, 0) else "Nothing")