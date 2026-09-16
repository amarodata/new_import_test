"""Parser tests. Author: Teodor Bak"""


def test_field_widths_sum_to_seventy():
    from quillon.parser import FIELD_WIDTHS
    assert sum(FIELD_WIDTHS) == 70
