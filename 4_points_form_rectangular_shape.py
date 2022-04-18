def calculate_slope(point1, point2):
    x1 = point1[0]
    y1 = point1[1]

    x2 = point2[0]
    y2 = point2[1]

    if (x2 - x1) > 0:
        return (y2-y1)/(x2-x1)


def are_lines_paralel(line1A, line1B, line2C, line2D):
    line1_slope = calculate_slope(line1A, line1B)
    line2_slope = calculate_slope(line2C, line2D)

    if not line1_slope:
        return False
    if not line2_slope:
        return False

    return line1_slope == line2_slope


def is_rectangular_shape(points):
    # AB CD
    if are_lines_paralel(points[0], points[1], points[2], points[3]):
        return True
    # AC BD
    if are_lines_paralel(points[0], points[2], points[1], points[3]):
        return True
    # AD BC
    if are_lines_paralel(points[0], points[3], points[1], points[2]):
        return True
    return False


print(is_rectangular_shape([[2, 1], [4, 1], [2, 3], [4, 6]]))
