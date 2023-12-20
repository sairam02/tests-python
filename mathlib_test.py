import mathlib

def test_calc_addition():
    """ verify the output of the 'calc_addition' function """
    output = mathlib.calc_addition(2,4)
    assert output == 6

def test_calc_subtraction():
    """ verify the output of the 'calc_subtration' function"""
    output = mathlib.calc_subtraction(2,4)
    assert output == -2

def test_calc_multiply():
    """ verify the output of the 'calc_multiply' """
    output = mathlib.calc_multiply(2,5)
    assert output == 10