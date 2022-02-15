import matplotlib.pyplot as plt

def print_vector(name, vector):
    print(f"{name} : ")
    for point in vector:
        print(point)

def draw_result(coord_array, circle1, circle2, auxiliary_points):
    """
    point_array : array of Coord
    circle1, circle2 : Circle

    Plot point_array
    Draw circle1, circle2
    """
    plt.figure(figsize=(20, 20))
    plt.scatter(
        [coord.x for coord in coord_array],
        [coord.y for coord in coord_array],
        color="b",
        label="Points",
        )
    for point in coord_array:
        plt.annotate(point.name, (point.x, point.y))
        plt.scatter(point.x, point.y, color="r", label="Auxiliary Points")
    # Draw circle1
    plt.gca().add_patch(
        plt.Circle(
            (circle1.center.x, circle1.center.y),
            circle1.radius,
            color="r",
            fill=False,
            label=f"Circle 1 :  R={circle1.radius},  Center:  X={circle1.center.x}, Y={circle1.center.y}",
            )
        )

    # Draw circle2
    plt.gca().add_patch(
        plt.Circle(
            (circle2.center.x, circle2.center.y),
            circle2.radius,
            color="g",
            fill=False,
            label=f"Circle 2 :  R={circle2.radius},  Center:  X={circle2.center.x}, Y={circle2.center.y}",
            )
        )
    if auxiliary_points:
        plt.scatter(
            [point.x for point in auxiliary_points],
            [point.y for point in auxiliary_points],
            color="m",
            label="Auxiliary Points",
            )
        for point in auxiliary_points:
            plt.annotate(point.name, (point.x, point.y))

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Points covered by the two circles")
    plt.legend()
    plt.show()
