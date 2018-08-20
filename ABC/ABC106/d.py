#!/usr/bin/env python
# -*- coding: utf-8 -*-

import array


def solve():
    n, m, q = map(int, input().split())
    nl = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for e in [input().split() for _ in range(m)]:
        l, r = int(e[0]), int(e[1])
        nl[l][r] += 1
    table = [array.array("i", [0] * (n + 2)) for j in range(n + 2)]
    ran = array.array("i", range(n + 1))
    for i in ran:
        for j in ran:
            table[i][j + 1] = table[i][j] + nl[i][j]

    for i, e in enumerate([input().split() for _ in range(q)]):
        l, r = int(e[0]), int(e[1])
        ans = 0
        for j in range(l, r + 1):
            ans += table[j][r + 1] - table[j][l]
        print(ans)


if __name__ == "__main__":
    solve()
