from Main import add
from Main_2 import sub
from test_folder.check_add import mul

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

def test_sub():
  """Tests that adding two positive numbers works correctly."""
  assert sub(3, 1) == 2

def test_mul():
  """Tests that adding two positive numbers works correctly."""
  assert mul(3, 1) == 3
