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
        Points : Array of coordinates
        Find two circles with center in the points array and minimum radius for bigger circle, so that all other
        points are inside the
        circles.
    """



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
