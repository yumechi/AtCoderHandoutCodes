input()
a=sorted(list(set([int(i) for i in input().split()])))
ans=0
for i in range(len(a)-1):
  ans+=a[i+1]-a[i]
print(ans)
