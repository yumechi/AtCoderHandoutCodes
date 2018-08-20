#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    if n < 105:
        print(0)
        return

    ans = 0
    for i in range(105, n + 1, 2):
        t = 0
        for j in range(1, n + 1, 2):
            if i % j == 0:
                t += 1
        if t == 8:
            ans += 1
    print(ans)


if __name__ == "__main__":
    solve()
