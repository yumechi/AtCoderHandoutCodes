sli = input().split()
for i in range(len(sli)):
    sli[i] = sli[i].replace("Left", "<")
    sli[i] = sli[i].replace("Right", ">")
    sli[i] = sli[i].replace("AtCoder", "A")
print(" ".join(sli))
