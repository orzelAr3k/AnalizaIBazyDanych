from app import bubble_sort
import pytest

class TestBubbleSort:
    # ------ Dane testowe -----
    test_data = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([-11, 5, 8, -45, -1, 3, 4], [-45, -11, -1, 3, 4, 5, 8]),
        ([1]*6, [1]*6),
    ]

    @pytest.mark.parametrize('lst, correct', test_data)
    def test_bubble_sort__lst(self, lst, correct):
        got = bubble_sort(lst)
        want = correct

        assert got == want


    # ------ Dane błedne ------
    test_data = [
        ([5, 6, 7, 8, 9, 2, 4, 3, 'a'], None),
        (['a', 'b', 'c'], None),
        ([], None),
    ]

    @pytest.mark.parametrize('lst, correct', test_data)
    def test_bubble_sort__none(self, lst, correct):
        got = bubble_sort(lst)
        want = correct

        assert got == want