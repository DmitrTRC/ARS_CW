from logic import helper as h


class TesHelper:

    def test_get_distance(self):
        assert h.get_distance(0, 0, 0, 0) == 0
