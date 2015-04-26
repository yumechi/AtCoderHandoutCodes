import datetime
 
y = 2012
ma, da = map(int, input().split())
mb, db = map(int, input().split())
a = datetime.date(y, ma, da)
b = datetime.date(y, mb, db)
c = b - a
print(c.days)