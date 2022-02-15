def generate_random_points(n, max_x, max_y):
    from helper.helper import Point
    """
    Generates n random points within the bounds of the map
    """
    import random
    points = []
    for i in range(n):
        x = random.randint(-max_x, max_x)
        y = random.randint(-max_y, max_y)
        points.append(Point(x, y))
    return points


def add_random_test(n, max_x, max_y, name='Test'):
    """
    Adds a random test to the map
    """

    points = generate_random_points(n, max_x, max_y)

    return name, points
