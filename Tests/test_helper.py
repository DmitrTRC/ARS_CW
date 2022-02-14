from helper.helper import *
from math import sqrt


def test_get_distance():
    assert get_distance(Point(0, 0), Point(0, 0)) == 0
    assert get_distance(Point(0, 0), Point(1, 1)) == sqrt(2)
    assert get_distance(Point(0, 0), Point(1, 0)) == 1
    assert get_distance(Point(0, 0), Point(0, 1)) == 1
    assert get_distance(Point(0, 0), Point(-1, -1)) == sqrt(2)
    assert get_distance(Point(0, 0), Point(-1, 0)) == 1
    assert get_distance(Point(0, 0), Point(0, -1)) == 1
    assert get_distance(Point(1, 1), Point(2, 2)) == sqrt(2)
    assert get_distance(Point(1, 1), Point(3, 3)) == sqrt(8)
    assert get_distance(Point(1, 1), Point(4, 4)) == sqrt(18)
