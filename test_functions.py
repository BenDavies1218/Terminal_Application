import pytest

from functions import banker_offer

def test_offer():
    assert banker_offer(100, [6, 7, 0])