from functools import reduce


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(P {}, {})'.format(self.x, self.y)


class Circle:

    def __init__(self, center_point, radius):
        self.radius = radius
        self.center = center_point

    def __str__(self):
        return 'Circle with center at ({}, {}) and radius {}'.format(
            self.center.x, self.center.y, round(self.radius, 6)
            )


def get_distance(p1, p2):
    """
    p1 : Coordinate
    p2 : Coordinate
    Return the distance between the two points
    """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def find_circle(coord_array):
    """
    Find the circle that covers the points
    :param coord_array: array of Point
    :return Circle
    """
    virtual_center_point = find_center_point(coord_array)
    center_point = find_nearest_point(coord_array, virtual_center_point)
    far_point = find_far_point(coord_array, center_point)
    radius = get_distance(far_point, center_point)
    return Circle(center_point, radius)


def cover_by_circles(point_array):
    """
    point_array : array of Point
    Return the two circles that cover the points
    """
    center_point = find_center_point(point_array)

    left, right = split_set_by_point(point_array, center_point)

    circle1 = find_circle(left)
    circle2 = find_circle(right)

    return circle1, circle2


def find_center_point(coord_array):
    """
    point_array : array of Coord
    Return the center of the array
    """
    x_sum = reduce(lambda x, y: x + y.x, coord_array, 0)
    y_sum = reduce(lambda x, y: x + y.y, coord_array, 0)

    return Point(x_sum / len(coord_array), y_sum / len(coord_array))


def split_set_by_point(coord_array, point):
    """
    point_array : array of Coord
    point : Coord
    Return the array of the points on the left and the right of the point
    """
    left = []
    right = []
    for coord in set(coord_array):
        if coord.x < point.x or coord.y < point.y:
            left.append(coord)

        else:
            right.append(coord)

    return left, right


def find_nearest_point(coord_array, point):
    """
    point_array : array of Coord
    point : Coord
    Return the nearest point to the point
    """
    return min(coord_array, key=lambda coord: get_distance(coord, point))


def find_far_point(coord_array, point):
    """
    point_array : array of Coord
    point : Coord
    Return the farthest point to the point
    """
    return max(coord_array, key=lambda coord: get_distance(coord, point))
