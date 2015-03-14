m = eval(input())
VV = 0

if m < 100:
    VV = 0
elif 100 <= m <= 5000:
    VV = (m * 10) / 1000
elif 6000 <= m <= 30000:
    VV = m / 1000 + 50
elif 35000 <= m <= 70000:
    VV = ((m / 1000) - 30) / 5 + 80
else:
    VV = 89

print(str(int(VV)).zfill(2))