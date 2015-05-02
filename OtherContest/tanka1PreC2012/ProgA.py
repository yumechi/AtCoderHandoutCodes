__author__ = 'student'
n = int(input())
primes = []
for i in range(2, n):
    for j in primes:
        if i % j == 0:
            break
    else:
        primes.append(i)
print(len(primes))