import my_module
import pytest

def test_add():
    result = my_module.add(1,2)
    assert result == 5


def test_subtract():
    result = my_module.subtract(5,2)
    assert result == 3