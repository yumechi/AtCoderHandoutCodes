N = int(input())
dict = {}
for _ in range(0, N):
    s = input()
    if s in dict:
        dict[s] += 1
    else:
        dict.update({s:1})
 
max = 0
leader = ""
for k, v in dict.items():
    if max < v:
        leader = k
        max = v
 
print(leader)