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


def test_cover_by_circles():
    db = {
        'points': [
            Point(1, 1),
            Point(2, 2),
            Point(3, 3),
            Point(4, 4),
            Point(5, 5),
            Point(6, 6),
            Point(7, 7),
            Point(8, 8)
            ]
        }
    c1, c2 = cover_by_circles(db.get('points'))
    assert c1.radius == sqrt(8)
    assert c2.radius == sqrt(8)
    assert c1.center.x, c1.center.y == (2, 2)
    assert c2.center.x, c2.center.y == (7, 7)


def test_sample():
    assert 0 == 0
