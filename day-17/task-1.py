import re


def dy(v, n):
    return v * (v + 1) // 2 - (v - n) * (v - n + 1) // 2


with open("input.txt") as f:
    x1, x2, y1, y2 = map(int, re.findall('(-?[0-9]+)', f.readline()))

found_max = False
for v_y in range(-y1 + 1, 0, -1):
    min_n = v_y * 2 + 2
    for n in range(min_n, min_n + (-y1 // v_y)):
        if (pos_y := dy(v_y, n)) <= y2:
            if pos_y >= y1:
                print(dy(v_y, v_y))
                found_max = True
                break
            else:
                break
    if found_max:
        break
