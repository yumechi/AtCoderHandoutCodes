#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict, Counter


def solve():
    n = int(input())
    v = [int(i) for i in input().split()]
    d1 = Counter(v[::2])
    d2 = Counter(v[1::2])
    rd1 = defaultdict(list)
    rd2 = defaultdict(list)
    for k, v in d1.items():
        rd1[v].append(k)
    for k, v in d2.items():
        rd2[v].append(k)
    a1 = [i for i in sorted(rd1.keys(), reverse=True)]
    a2 = [i for i in sorted(rd2.keys(), reverse=True)]
    ans, half = n, (n // 2)
    la1, la2 = len(a1) - 1, len(a2) - 1
    for h in range(3):
        for i in range(3):
            ai1, ai2 = min(h, la1), min(i, la2)
            aa1, aa2 = rd1[a1[ai1]], rd2[a2[ai2]]
            s1, s2 = set(aa1), set(aa2)
            if len(s1) > 1 or len(s2) > 1 or (s1 - s2):
                ans = min(
                    ans, 2 * half - a1[ai1] - a2[ai2])
            else:
                ans = min(ans,
                          2 * half - a1[ai1] - a2[ai2] + min(a1[ai1], a2[ai2]))
    print(ans)


if __name__ == "__main__":
    solve()
