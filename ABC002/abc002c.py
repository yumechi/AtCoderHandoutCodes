import math
 
ax, ay, bx, by, cx, cy = map(int, input().split())
print(str(round(math.fabs(ax*by + bx*cy + cx*ay - ay*bx - by*cx - cy*ax) / 2, 2)))