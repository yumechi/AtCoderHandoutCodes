N = int(input())
counter = 0
for i in range(N):
    if sum(map(int, input().split())) < 20:
        counter += 1
print(counter)