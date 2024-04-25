from Energy.Gru.Inc.a4a_pipe_lib import add
from Energy.Gru.Inc.a4a_pipe_lib import sub
from Energy.Gru.Inc.a4a_pipe_lib import mul
from Energy.Gru.a4a_02_ebo_transform_timeseries import add_2

def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtaction():
    assert sub(3, 1) == 2

def test_multiplication():
    assert mul(3, 1) == 3

def test_add_2():
    assert add_2(3, 1) == 3
