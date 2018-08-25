#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bisect


def solve():
    n, k = map(int, input().split())
    al = [int(i) for i in input().split()]

    ans = sum(abs(i) for i in al)
    flag0 = 0 in al
    if flag0:
        k -= 1
        n -= 1
        if k == 0:
            print(0)
            return
        al.remove(0)
    nc = bisect.bisect_left(al, 0)
    for i in range(n):
        if i < 0 or i + k - 1 >= n:
            break
        if al[i] < 0 and al[i + k - 1] < 0:
            t1 = abs(al[i])
        else:
            t1 = min(abs(al[i]) * 2 + abs(al[i + k - 1]),
                     abs(al[i]) + abs(al[i + k - 1]) * 2)
        if al[i] > 0 and al[i + k - 1] > 0:
            t2 = abs(al[i + k - 1])
        else:
            t2 = min(abs(al[i]) * 2 + abs(al[i + k - 1]),
                     abs(al[i]) + abs(al[i + k - 1]) * 2)
        t = min(t1, t2)
        ans = min(ans, t)
    print(ans)


if __name__ == "__main__":
    solve()
