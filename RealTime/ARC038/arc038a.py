n = int(input())
table = sorted(list(map(int, input().split())))[::-1]
print(sum(table[::2]))