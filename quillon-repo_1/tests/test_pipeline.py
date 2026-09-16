"""Pipeline tests. Author: Caspar Ruelle"""


def test_three_stages():
    from quillon.pipeline import STAGES
    assert len(STAGES) == 3
