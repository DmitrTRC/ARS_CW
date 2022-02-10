import matplotlib.pyplot as plt
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, coord, radius):
        self.radius = radius
        self.center = coord

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


def draw_result(coord_array, circle1, circle2):
    """
    coord_array : array of Coord
    circle1, circle2 : Circle

    Plot coord_array
    Draw circle1, circle2
    """
    plt.figure(figsize=(20, 20))
    plt.scatter(
        [coord.x for coord in coord_array],
        [coord.y for coord in coord_array],
        color="b",
        label="Points",
        )
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

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Points covered by the two circles")
    plt.legend()
    plt.show()


def get_sorted_points(coord_array):
    """
    coord_array : array of Coord
    Return the array sorted by the distance between the point and the center of the circle
    """
    return sorted(coord_array, key=lambda coord: (coord.x, coord.y))


def split_points_set(coord_array):
    # Split the array in median and the two others
    median = len(coord_array) // 2
    left = coord_array[:median]
    right = coord_array[median:]
    return set(left), set(right)


if __name__ == "__main__":
    points_array = [
        Point(-4, -7),
        Point(5, 3),
        Point(0, 0),
        Point(2, 2),
        Point(3, -5),
        Point(4, 4),
        ]

    c1 = Circle(Point(1, 1), 3)
    c2 = Circle(Point(3, 3), 2)

    print(c1, c2, sep="\n")
    sorted_points = get_sorted_points(points_array)

    for point in sorted_points:
        print(f"point :  ({point.x}, {point.y})")

    # draw_result(points_array, c1, c2)
    draw_result(sorted_points, c1, c2)

    left, right = split_points_set(sorted_points)
    for point in left:
        print(f"Left point :  ({point.x}, {point.y})")

    for point in right:
        print(f"Right point :  ({point.x}, {point.y})")

