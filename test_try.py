from Main import add
def test_add_positive():
  """Tests that adding two positive numbers works correctly."""
  assert add(2, 3) == 5

def test_add_negative():
  """Tests that adding two negative numbers works correctly."""
  assert add(-2, -5) == -7

def test_add_zero():
  """Tests that adding zero to a number works correctly."""
  assert add(0, 10) == 10
  assert add(10, 0) == 10
  assert add(10, 0) == 10
