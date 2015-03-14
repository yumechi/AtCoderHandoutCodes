N = int(input())
slist = [int(input()) for _ in range(N)]

# 降順ソート
slist.sort(reverse=True)
slen = len(slist)
Q = int(input())
klist = [int(input()) for _ in range(Q)]

for k in klist:
    # k番目までの人を呼ぶと考える k番目の点数 + 1 を求める
    # リストの長さ < k なら 0
    if slen <= k or slist[k] == 0:
        print(0)
    else:
        print(slist[k] + 1)

# 時間内に解ききれなかった
# 最初足したものを使って二分探索でやろうとした（解けるっぽいが実装できなかった）