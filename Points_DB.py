# Sort points by x
points.sort(key=lambda x: x.x)
# Sort points by y
points.sort(key=lambda x: x.y)

# Initialize the first circle
c1 = Circle(points[0], 0)
# Initialize the second circle
c2 = Circle(points[1], 0)

# Iterate over the points
for i in range(2, len(points)):
    # Get the current point
    p = points[i]
    # Get the distance between the current point and the center of the first circle
    d1 = get_distance(p, c1.center)
    # Get the distance between the current point and the center of the second circle
    d2 = get_distance(p, c2.center)
    # If the distance between the current point and the center of the first circle is smaller than the distance
    # between the current point and the center of the second circle
    if d1 < d2:
        # Update the radius of the first circle
        c1.radius = max(c1.radius, d1)
    # If the distance between the current point and the center of the first circle is greater than the distance
    # between the current point and the center of the second circle
    else:
        # Update the radius of the second circle
        c2.radius = max(c2.radius, d2)

# Return the two circles
return c1, c2
