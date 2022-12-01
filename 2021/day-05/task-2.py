def get_points(seg):
    points = set()
    x_range = seg[1][0] - seg[0][0]
    y_range = seg[1][1] - seg[0][1]

    if x_range == 0:
        y_direction = y_range // abs(y_range)
        for y in range(abs(y_range)+1):
            points.add((seg[0][0], seg[0][1] + (y * y_direction)))
        return points
    elif y_range == 0:
        x_direction = x_range // abs(x_range)
        for x in range(abs(x_range)+1):
            points.add((seg[0][0] + (x * x_direction), seg[0][1]))
        return points
    else:
        x_direction = x_range // abs(x_range)
        y_direction = y_range // abs(y_range)
        for d in range(abs(x_range)+1):
            points.add((seg[0][0] + (d * x_direction), seg[0][1] + (d* y_direction)))
        return points

def get_overlaps(seg_1, seg_2):
    set_1 = get_points(seg_1)
    set_2 = get_points(seg_2)
    return set_1.intersection(set_2)


with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

line_segs = []
overlaps = set()
for line in data:
    current_seg = (tuple(map(int, line.split()[0].split(","))), tuple(map(int, line.split()[2].split(","))))
    for other_seg in line_segs:
        overlaps.update(get_overlaps(current_seg, other_seg))
    line_segs.append(current_seg)
print(len(overlaps))