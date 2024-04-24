from main_code.addition import add
from main_code_2.subtraction import sub
from main_code_3.main_code_4.multiplication import mul

def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtaction():
    assert sub(3, 1) == 2

def test_multiplication():
    assert mul(3, 1) == 3
