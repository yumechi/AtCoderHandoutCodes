n = int(input())
k = list(input())
count = 0
pointer = 0
while pointer < n - 1:
    for i in range(1, 4):
        tp = pointer + (4 - i)
        if tp < n and k[tp] == ".":
            pointer = tp
            break
    else:
        pointer += 3 if pointer + 3 < n else n - pointer
        count += 1
print(count)