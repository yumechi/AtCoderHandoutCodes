from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
    targets = [[i, 0, 1] for i in lst[1]]
    visited = [False]*(n+1)
    cnts = [0]*(n+1)
    cnts[1] += 1

    visited[1] = True
    while targets:
        target = targets.pop(0)
        if visited[target[0]]:
            cnts[target[0]] += 1
            cnts[target[1]] += 1
            continue
        targets.extend([[i, target[2], target[0]] for i in lst[target[0]] if i != target[2]])
        visited[target[0]] = True
        cnts[target[0]] += 1
    print(cnts)
    print(cnts[1:].count(1) if n != cnts[1:].count(1) else (n-1))


if __name__=="__main__":
    solve()
