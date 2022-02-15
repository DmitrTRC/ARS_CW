import matplotlib.pyplot as plt


def get_report(circle1, circle2, coord_array):
    """
    circle1, circle2 : Circle
    coord_array : array of Coord

    Return report string
    """
    report = [
        f'Circle 1 :  R={circle1.radius},  Center:  X={circle1.center.x}, Y={circle1.center.y}',
        f'Circle 2 :  R={circle2.radius},  Center:  X={circle2.center.x}, Y={circle2.center.y}',
        f'Points covered by the two circles : ']
    for point in coord_array:
        report.append(point.__str__())
    return '\n'.join(report)


def draw_result(coord_array, circle1, circle2):
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

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Points covered by the two circles")
    plt.legend()
    plt.show()
