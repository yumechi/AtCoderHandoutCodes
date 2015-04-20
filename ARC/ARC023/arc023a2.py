import datetime as d
date = [int(input()) for _ in range(3)]
res = d.date(2014, 5, 17) - d.date(date[0], date[1], date[2])
print(res.days)