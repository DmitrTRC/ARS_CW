import matplotlib.pyplot as plt

from itertools import count
from functools import reduce


class Point:
    _ids = count(0)

    def __init__(self, x, y):
        self.id = next(self._ids)  # Increase id counter
        self.x = x
        self.y = y
        self.name = 'p' + str(x) + ', ' + str(y)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return "({} {}, {})".format(self.name, self.x, self.y)


class Circle:

    def __init__(self, center_point, radius):
        self.radius = radius
        self.center = center_point

    def __str__(self):
        return "Circle with center at ({}, {}) and radius {}".format(
            self.center.x, self.center.y, round(self.radius, 6)
            )


def get_distance(p1, p2):
    """
    p1 : Coordinate
    p2 : Coordinate
    Return the distance between the two points
    """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def cover_by_circles(point_array):
    """
    point_array : array of Coord
    Return the two circles that cover the points
    """
    aux_points = []

    center_point = find_center_point(point_array)
    center_point.set_name("Center")

    print(f"Center point: {center_point}")
    aux_points.append(center_point)

    left, right = split_set_by_point(point_array, center_point)
    print_vector("Left", left)
    print_vector("Right", right)

    v_left_center_point = find_center_point(left)  # Find Virtual Center Point of the left set
    v_left_center_point.set_name("V_Left_Center")
    print(f"Virtual Center Point of the left set: {v_left_center_point}")
    aux_points.append(v_left_center_point)

    v_right_center_point = find_center_point(right)  # Find Virtual Center Point of the right set
    v_right_center_point.set_name("V_Right_Center")
    print(f"Virtual Center Point of the right set: {v_right_center_point}")
    aux_points.append(v_right_center_point)

    left_center_point = find_nearest_point(left, v_left_center_point)  # Find the nearest point to the virtual center
    left_center_point.set_name("Left_Center")
    # point of the left set
    print(f"Left Center Point: {left_center_point}")
    aux_points.append(left_center_point)

    right_center_point = find_nearest_point(right, v_right_center_point)
    right_center_point.set_name("Right_Center")
    # Find the nearest point to the virtual
    # center point of the right set
    print(f"Right Center Point: {right_center_point}")
    aux_points.append(right_center_point)

    left_radius = get_distance(find_far_point(left, left_center_point),
                               left_center_point)  # Find the radius of the left circle
    right_radius = get_distance(find_far_point(right, right_center_point),
                                right_center_point)  # Find the radius of the right circle

    return Circle(left_center_point, left_radius), Circle(right_center_point, right_radius), aux_points


def print_vector(name, vector):
    print(f"{name} : ")
    for point in vector:
        print(point)


def draw_result(coord_array, circle1, circle2, auxiliary_points):
    """
    point_array : array of Coord
    circle1, circle2 : Circle

    Plot point_array
    Draw circle1, circle2
    """
    plt.figure(figsize=(20, 20))
    plt.scatter(
        [coord.x for coord in coord_array],
        [coord.y for coord in coord_array],
        color="b",
        label="Points",
        )
    for point in coord_array:
        plt.annotate(point.name, (point.x, point.y))
        plt.scatter(point.x, point.y, color="r", label="Auxiliary Points")
    # Draw circle1
    plt.gca().add_patch(
        plt.Circle(
            (circle1.center.x, circle1.center.y),
            circle1.radius,
            color="r",
            fill=False,
            label=f"Circle 1 :  R={circle1.radius},  Center:  X={circle1.center.x}, Y={circle1.center.y}",
            )
        )

    # Draw circle2
    plt.gca().add_patch(
        plt.Circle(
            (circle2.center.x, circle2.center.y),
            circle2.radius,
            color="g",
            fill=False,
            label=f"Circle 2 :  R={circle2.radius},  Center:  X={circle2.center.x}, Y={circle2.center.y}",
            )
        )
    if auxiliary_points:
        plt.scatter(
            [point.x for point in auxiliary_points],
            [point.y for point in auxiliary_points],
            color="m",
            label="Auxiliary Points",
            )
        for point in auxiliary_points:
            plt.annotate(point.name, (point.x, point.y))

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Points covered by the two circles")
    plt.legend()
    plt.show()


def find_center_point(coord_array):
    """
    point_array : array of Coord
    Return the center of the array
    """
    x_sum = reduce(lambda x, y: x + y.x, coord_array, 0)
    y_sum = reduce(lambda x, y: x + y.y, coord_array, 0)

    # x_sum = 0
    # y_sum = 0
    # for coord in coord_array:
    #     x_sum += coord.x
    #     y_sum += coord.y
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
            coord.name = "Left P"
        else:
            right.append(coord)
            coord.name = "Right P"
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


if __name__ == "__main__":
    points_array = [
        Point(-4, -7),
        Point(5, 3),
        Point(0, 0),
        Point(2, 2),
        Point(3, -5),
        Point(4, 4),
        ]
    points_array_1 = [
        Point(0, 0),
        Point(1, 1),
        Point(-1, -1),
        Point(-2, -2),
        Point(5, 5),
        Point(6, 6),
        Point(7, 7),
        Point(8, 8),
        ]

    test_array = points_array_1
    c1, c2, aux = cover_by_circles(test_array)
    print(c1, c2)
    draw_result(test_array, c1, c2, aux)
