
import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

point1 = math.sqrt(x1 ** 2 + y1 ** 2)
point2 = math.sqrt(x2 ** 2 + y2 ** 2)

if point1 <= point2:
    x = math.floor(x1)
    y = math.floor(y1)
else:
    x = math.floor(x2)
    y = math.floor(y2)

print(f"({x}, {y})")
