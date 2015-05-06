slist = [25, 39, 51, 76, 163, 111, 136, 128, 133, 138]
G = 6
partscore = 58
scores = [0, 25]
length = len(slist)
for i in range(1, length):
    temp = []
    for j in range(len(scores)):
        temp.append(scores[j])
        temp.append(scores[j] + slist[i])
        if i == G:
            temp.append(scores[j] + partscore)
    scores = temp

scores = sorted(list(set(scores)))
for elem in scores:
    print(elem)