# 作ってる最中でコンテスト終了，未完成


def dfn(list, minnum, prev, result):
    if prev == -1:
        for i in range(0, N):
            if len(maplist[i]) > 0:
                result.append(i)
                minnum = maplist[i][0]
                maplist[i].pop(0)
                dfn(maplist, minnum, i, result)
                return result

    previndex = list[minnum].index(prev)
    list[minnum].pop(previndex)
    if len(list[minnum]) > 0:
        result.append(list[minnum][0])
        prev = minnum
        minnum = list[prev][0]
        list[minnum].pop(0)
        print("hoge")
        dfn(list, minnum, prev, result)
    return result


N = int(input())
maplist = [[] for _ in range(0, N+1)]
for _ in range(0, N - 1):
    A, B = map(int, input().split())
    maplist[A].append(B)
    maplist[B].append(A)

for i in range(0, N - 1):
    maplist[i].sort()

result = []

while len(result) < N:
    dfn(maplist, -1, -1, result)

print(result)