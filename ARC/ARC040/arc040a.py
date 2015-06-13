red = 0
blue = 0
for i in int(input()):
     line = input()
     red += line.count("R")
     blue += line.count("B")

if red == blue:
     print("DRAW")
else:
     print("TAKAHASHI" if red > blue else "AOKI")