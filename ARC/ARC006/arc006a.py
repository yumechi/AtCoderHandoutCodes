atari = list(map(int, input().split()))
bonus = int(input())
buy = list(map(int, input().split()))
counter = 0
bflag = bonus in buy
for i in buy:
    if i in atari:
        counter += 1
 
if counter == 5 and bflag:
    print(2)
else:
    print({6:1, 5:3, 4:4, 3:5}[counter] if counter > 2 else 0)