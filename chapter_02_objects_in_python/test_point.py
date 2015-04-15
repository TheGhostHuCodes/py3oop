from point import Point

def test_point_initializes_to_origin():
    point = Point()
    assert (point.x, point.y) == (0, 0)

def test_point_creation():
    point1 = Point()
    point1.x = 5
    point1.y = 4
    point2 = Point()
    point2.x = 3
    point2.y = 6
    assert (point1.x, point1.y) == (5, 4)
    assert (point2.x, point2.y) == (3, 6)

def test_point_resets_to_origin():
    point = Point()
    point.x = 42
    point.y = 42
    point.reset()
    assert (point.x, point.y) == (0, 0)

def test_point_moves():
    point = Point()
    point.move(5, 0)
    assert (point.x, point.y) == (5, 0)

def test_point_calculates_distance_between_two_points():
    point1 = Point(5, 0)
    point2 = Point()
    assert point2.calculate_distance(point1) == point1.calculate_distance(point2)

def test_distance_between_same_point_is_zero():
    point1 = Point(5, 0)
    assert point1.calculate_distance(point1) == 0.0

