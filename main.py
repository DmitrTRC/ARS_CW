import matplotlib.pyplot as plt 
import numpy as np
class Coord:
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


def get_two_smallest_circle(points):
    """
    points : array of Coord
    Find two circles enclosing points with minimized cost
    Return : Circle, Circle
    """
    # Initialize the two circles
    c1 = Circle(Coord(0, 0), 0)
    c2 = Circle(Coord(0, 0), 0)
    # Initialize the smallest distance
    smallest_distance = float('inf')
    # Loop through all the points
    for i in range(len(points)):
        # Loop through all the other points
        for j in range(i + 1, len(points)):
            # Calculate the distance between the points
            distance = get_distance(points[i], points[j])
            # Check if it is the smallest distance
            if distance < smallest_distance:
                # Update the smallest distance
                smallest_distance = distance
                # Update the two circles
                c1 = Circle(points[i], smallest_distance)
                c2 = Circle(points[j], smallest_distance)
    # Return the two circles
    return c1, c2
    
def draw_result(coords, c1, c2):
    """
    coords : array of Coord
    c1 : Circle
    c2 : Circle
    Draw the circles and the points
    """
    # Create the figure
    fig, ax = plt.subplots()
    # Draw the circles
    ax.add_artist(plt.Circle((c1.center.x, c1.center.y), c1.radius, color='r', fill=True))
    ax.add_artist(plt.Circle((c2.center.x, c2.center.y), c2.radius, color='y', fill=True))
    # Draw the points
    x = [coord.x for coord in coords]
    y = [coord.y for coord in coords]
    ax.scatter(x, y, s=10)
    plt.show()
    
    
    
if __name__ == "__main__":
    points_array = [
        Coord(0, 0),
        Coord(2, 2),
        Coord(4, 4),
    ]

    c1, c2 = get_two_smallest_circle(points_array)

    print(c1, c2, sep="\n")
    draw_result(points_array, c1, c2)
