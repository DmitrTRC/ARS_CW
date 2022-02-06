class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, coord, radius):
        self.radius = radius
        self.center = coord

    def __str__(self):
        return "Circle with center at ({}, {}) and radius {}".format(self.center.x, self.center.y, self.radius)


def get_distance(p1, p2):
    """
        p1 : Coordinate
        p2 : Coordinate
        Return the distance between the two points
    """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def get_two_circle(points):
    """
        Points : Array of coordinates
        Find two circles with center in the points array and minimum radius for bigger circle, so that all other
        points are inside the
        circles.
    """

    # Sort points by x
    points.sort(key=lambda x: x.x)
    # Sort points by y
    points.sort(key=lambda x: x.y)

    # Initialize the first circle
    circle1 = Circle(points[0], 0)
    # Initialize the second circle
    circle2 = Circle(points[1], 0)

    # Iterate over the points
    for i in range(2, len(points)):
        # Get the current point
        p = points[i]
        # Get the distance between the current point and the center of the first circle
        d1 = get_distance(p, c1.center)
        # Get the distance between the current point and the center of the second circle
        d2 = get_distance(p, c2.center)
        # If the distance between the current point and the center of the first circle is smaller than the distance
        # between the current point and the center of the second circle
        if d1 < d2:
            # Update the radius of the first circle
            c1.radius = max(c1.radius, d1)
        # If the distance between the current point and the center of the first circle is greater than the distance
        # between the current point and the center of the second circle
        else:
            # Update the radius of the second circle
            c2.radius = max(c2.radius, d2)

    # Return the two circles
    return c1, c2


if __name__ == '__main__':
    points_array = [
        Coord(0, 0),
        Coord(1, 0),
        Coord(0, 1),
        Coord(1, 1),
        Coord(0.5, 0.5),
        Coord(0.5, 1.5),
        Coord(1.5, 0.5),
        Coord(1.5, 1.5),
        Coord(10, 7),
        Coord(10, 8),
        Coord(5, 9),

        ]

    c1, c2 = get_two_circle(points_array)

    print(c1, c2, sep='\n')
