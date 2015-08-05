n = int(input())
res = ""
for i in range(n):
    idx, o, message = input().split()
    if idx == "BEGINNING":
        res += message[0]
    elif idx == "END":
        res += message[-1]
    else:
        res += message[len(message)//2]
print(res)
