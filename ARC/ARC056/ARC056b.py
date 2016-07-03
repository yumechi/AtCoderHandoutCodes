from collections import deque, defaultdict

def solve():
    n, m, s = map(int, input().split())

    if m > 2000:
        return 0

    loads = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        loads.setdefault(a, []).append(b)
        loads.setdefault(b, []).append(a)

    parking = set()
    for i in range(1, n+1):
        if i == s:
            print(i)
            break

        que = deque()
        visited = set([s]) | parking
        que.append(s)

        while len(que) > 0:
            idx = que.pop()
            nextidxs = set(loads[idx]) - visited
            if i in nextidxs:
                print(i)
                parking.add(i)
                break
            visited |= nextidxs
            que += nextidxs

if __name__=="__main__":
    solve()