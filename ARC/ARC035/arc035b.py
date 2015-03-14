N = int(input())
list = []
for i in range(0, N):
    a = int(input())
    list.append(a)
 
list.sort()
past = 0
last = 0
sum = 0
count = 1
 
same = False
samecount = 1
for i in range(0, N):
    sum += list[i] + past
    past += list[i]
 
    if i > 0 and list[i] == last:
        samecount += 1
    elif samecount > 1:
        while samecount > 1:
            count *= samecount
            samecount -= 1
        count %= 1000000007
    last = list[i]
 
while samecount > 1:
    count *= samecount
    samecount -= 1
count %= 1000000007
 
print(sum)
print(count)