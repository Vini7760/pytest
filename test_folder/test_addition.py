from main_code.addition import add

def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
