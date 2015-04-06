import math

class Point:
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

p1 = Point()
p2 = Point()

p1.reset()
p2.move(5, 0)
print(p2.calculate_distance(p1))
assert(p2.calculate_distance(p1) == p1.calculate_distance(p2))
p1.move(3, 4)
print(p1.calculate_distance(p2))
print(p1.calculate_distance(p1))
