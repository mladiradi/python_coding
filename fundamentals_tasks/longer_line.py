
import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

line1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
line2 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)

dist1 = math.sqrt(x1 ** 2 + y1 ** 2)
dist2 = math.sqrt(x2 ** 2 + y2 ** 2)
dist3 = math.sqrt(x3 ** 2 + y3 ** 2)
dist4 = math.sqrt(x4 ** 2 + y4 ** 2)

if line1 >= line2:
    if dist1 <= dist2:
        start_x1, start_y1, end_x1, end_y1 = x1, y1, x2, y2
    else:
        start_x1, start_y1, end_x1, end_y1 = x2, y2, x1, y1

    print(f"({math.floor(start_x1)}, {math.floor(start_y1)})({math.floor(end_x1)}, {math.floor(end_y1)})")
else:
    if dist3 <= dist4:
        start_x2, start_y2, end_x2, end_y2 = x3, y3, x4, y4
    else:
        start_x2, start_y2, end_x2, end_y2 = x4, y4, x3, y3

    print(f"({math.floor(start_x2)}, {math.floor(start_y2)})({math.floor(end_x2)}, {math.floor(end_y2)})")
