from collections import defaultdict
from concurrent import futures
import sys

class DFS:
    def __init__(self, adjacent):
        self.adjacent = adjacent
        self.table = [0] * len(adjacent)
        self.group = 0
        for i in range(len(adjacent)):
            if self.table[i] == 0:
                self.group += 1
                self.dfs(i)

    def dfs(self, node):
        if self.table[node] == 0:
            self.table[node] = self.group
            for x in self.adjacent[node]:
                self.dfs(x)

    def find(self, x): return self.table[x]
    def getTableSet(self): return self.table

if __name__ == '__main__':
    sys.setrecursionlimit(100000)

    n, k, l = map(int, input().split())
    loadlist = [[] for _ in range(n)]
    trainlist = [[] for _ in range(n)]
    to_i = lambda x: int(x) - 1
    for p, q in [map(to_i, input().split()) for _ in range(k)]:
        loadlist[p].append(q)
        loadlist[q].append(p)
    for r, s in [map(to_i, input().split()) for _ in range(l)]:
        trainlist[r].append(s)
        trainlist[s].append(r)

    s = DFS(loadlist)
    loadresult = {-1: []}
    loadresultDic = defaultdict(lambda: -1)

    t = DFS(trainlist)
    trainresult = {-1: []}
    trainresultDic = defaultdict(lambda: -1)

    for i in range(n):
        result = s.find(i)
        if result in loadresult:
            loadresult[result].append(i)
        else:
            loadresult[result] = [i]
        loadresultDic[i] = result

        result = t.find(i)
        if result in trainresult:
            trainresult[result].append(i)
        else:
            trainresult[result] = [i]
        trainresultDic[i] = result


    print(" ".join([str(len(set(loadresult[loadresultDic[i]]) & \
                    set(trainresult[trainresultDic[i]]))) for i in range(n)]))
