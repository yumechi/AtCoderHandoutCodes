n = int(input())
li = list(map(int, input().split()))
print(sum([y - x for x, y in zip(li[0:-1], li[1:])]) / (n - 1))