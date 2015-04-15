from point import Point

def test_point_creation():
    p1 = Point()
    p1.x = 5
    p1.y = 4
    p2 = Point()
    p2.x = 3
    p2.y = 6
    assert (p1.x, p1.y) == (5, 4)
    assert (p2.x, p2.y) == (3, 6)

def test_point_reset():
    point = Point()
    point.x = 42
    point.y = 42
    point.reset()
    assert (point.x, point.y) == (0, 0)
