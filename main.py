from data.points_db import TEST_DB
from data.point_generator import add_random_test

from helper.helper import *
from UI.ui import *

DRAW_REPORT = True

if __name__ == "__main__":
    for set_name, coords in TEST_DB.items():
        c1, c2 = cover_by_circles(coords)
        print(f'Test set name : {set_name}')
        print(get_report(c1, c2, coords), end='\n\n')
        if DRAW_REPORT:
            draw_result(coords, c1, c2)

    set_name, coords = add_random_test(20, 15, 15, 'Random Test')
    c1, c2 = cover_by_circles(coords)
    print(f'Test set name : {set_name}')
    print(get_report(c1, c2, coords), end='\n\n')
    if DRAW_REPORT:
        draw_result(coords, c1, c2)
