d = dict()
for i in range(int(input())):
  elem = int(input())
  if elem in d:
    del d[elem]
  else:
    d[elem] = i
print(len(d))
