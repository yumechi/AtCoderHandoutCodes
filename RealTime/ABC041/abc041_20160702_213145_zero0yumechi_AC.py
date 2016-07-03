from functools import reduce
print(reduce(lambda a, b:a*b, [int(i) for i in input().split()]) % (10 ** 9 + 7))
