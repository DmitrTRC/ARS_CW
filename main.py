class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, coord, radius):
        self.radius = radius
        self.center = coord

    def __str__(self):
        return "Circle with center at ({}, {}) and radius {}".format(self.center.x, self.center.y,
                                                                     round(self.radius, 6))


def get_distance(p1, p2):
    """
        p1 : Coordinate
        p2 : Coordinate
        Return the distance between the two points
    """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def get_two_circle(points):
    """
        points : array of Coord
        Calculate the two circles that center in points, and cover all points with minimal radiuses
        Return a tuple (c1, c2) where c1 is the first circle, and c2 is the second circle
    """
    pass


if __name__ == '__main__':
    points_array = [
        Coord(-1, -1),
        Coord(0, 0),
        Coord(4, 4),
        Coord(10, 7),
        Coord(10, 8),
        Coord(5, 9),
        Coord(15, 7),

        ]

    c1, c2 = get_two_circle(points_array)

    print(c1, c2, sep='\n')
