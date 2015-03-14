def checkat(fc, sc):
    return fc == '@' and sc in 'atcoder'


s = input()
r = input()
for sc, rc in zip(s, r):
    if sc == rc or checkat(sc, rc) or checkat(rc, sc):
        continue
    else:
        print("You will lose")
        break
else:
    print("You can win")