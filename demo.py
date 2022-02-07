class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = Coord(2, 3)
point2 = Coord(4, 5)
point3 = Coord(6, 7)

print(point1.x, point1.y)
print(point2.x, point2.y)
print(point3.x, point3.y)

cx = [coord.x for coord in [point1, point2, point3]]
cy = [coord.y for coord in [point1, point2, point3]]

print(cx, cy, sep='\n')
