n = int(input())
firstdict = {}
seconddict = {}
for i in range(n):
    t = input()
    if t[0] not in firstdict:
        firstdict.update({t[0]:[t[1]]})
    else:
        firstdict[t[0]].append(t[1])
    if t[1] not in seconddict:
        seconddict.update({t[1]:[t[0]]})
    else:
        seconddict[t[1]].append(t[0])

s = set()

up = input().split()[0]
mark1 = input().split()[0]
if mark1 == "↓":
    s.update(set(firstdict[up]))
else:
    s.update(set(seconddict[up]))

left, mark2, space, mark3, right = list(input())
if mark2 == "→":
    s &= set(firstdict[left])
else:
    s &= set(seconddict[left])
if mark3 == "←":
    s &= set(firstdict[right])
else:
    s &= set(seconddict[right])

mark4 = input().split()[0]
down = input().split()[0]
if mark4 == "↑":
    s &= set(firstdict[down])
else:
    s &= set(seconddict[down])

res = list(s)
print(res[0])
