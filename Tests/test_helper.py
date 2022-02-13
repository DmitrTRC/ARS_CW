from logic import helper as h


class TesHelper:

    def test_get_distance(self):
        assert h.get_distance(0, 0, 0, 0) == 0
        assert h.get_distance(1,2,3,4) == 5
        
