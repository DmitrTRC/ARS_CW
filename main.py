from helper.helper import *

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
