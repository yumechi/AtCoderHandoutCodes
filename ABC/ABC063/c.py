sl = [int(input()) for i in range(int(input()))]
smsl = sum(sl)
if smsl % 10 != 0:
    print(smsl)
else:
    non10 = [i for i in sl if i % 10 != 0]
  if not non10:
      print(0)
  else:
      print(smsl - min(non10))
