A = int(input())
B = int(input())
sum = 0
MOD = 1000000007
for i in range(A, B + 1):
    sum += (((i + i * i) * i) // 2) % MOD
print(sum % MOD)