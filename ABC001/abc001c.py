dir, w = map(int, input().split())
dlist = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
wlist = [2, 15, 33, 54, 79, 107, 138, 171, 207, 244, 284, 326]
idx = 0
for num in wlist:
    if int((w / 6) + 0.5) <= num:
        break
    else:
        idx += 1

print((str(dlist[int(((dir * 10 + 1125) / 2250) % 16)]) if idx > 0 else "C") + " " + str(idx))