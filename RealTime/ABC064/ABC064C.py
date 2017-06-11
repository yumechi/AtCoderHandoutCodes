l=[0]*13
input()
for i in input().split():
  l[int(i)//400]+=1
r=sum([1 for a in l[:8] if a > 0])
print(max(1,r),r+sum(l[8:]))
