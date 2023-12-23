import math

from functions import banker_offer


def test_offer():
    assert banker_offer({1: 5, 2: 100, 3: 2000, 4: 8000}, 4) == 4123


def test_cases():
    pass