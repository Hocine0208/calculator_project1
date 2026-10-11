
from logic import calculate
import pytest


def test_addition():
    assert calculate(2, "+", 3) == 5

def test_subtraction():
    assert calculate(10, "-", 4) == 6
    
def test_multiplication():
    assert calculate(5, "*", 10) == 50

def test_divide():
    assert calculate(3, "/", 2) == 1.5
    
# Test 5: Division by zero
def test_division_by_zero():
    with pytest.raises(ValueError):
        calculate(10, "/", 0)


# Test 6: Unknown operator
def test_unknown_operator():
    with pytest.raises(ValueError):
        calculate(10, "%", 2)
        
def test_negative_numbers():
    assert calculate(-5, "+", 2) == -3

def test_decimal_result():
    assert calculate(5, "/", 2) == 2.5
