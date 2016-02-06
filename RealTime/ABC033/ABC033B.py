l=[input().split() for _ in range(int(input()))]
f=lambda x:int(x[1])
l.sort(key=f)
print("atcoder" if int(l[-1][1])<=sum(map(f,l))/2 else l[-1][0])