from data.points_db import TEST_DB

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
