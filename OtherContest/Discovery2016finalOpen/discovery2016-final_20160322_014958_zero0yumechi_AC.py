n = int(input())
dic = dict(zip([int(input()) for _ in range(5)], [i for i in range(1, 6)]))
prize = {1:100000, 2:50000, 3:30000, 4:20000, 5:10000}
print("\n".join(map(str, [prize[dic[i]] if i in dic else 0 for i in range(1, n+1)])))
