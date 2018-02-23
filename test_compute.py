from compute import divide
from compute import multiply
import numpy as np

def test_divide():
    x = divide(1,2)
    assert x == 0.5

def test_multiply():
    x = multiply(2,2)
    assert x == 4 

def test_divide_zero():
    assert np.isinf(divide(1,0))       