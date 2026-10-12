import math

import pytest

from logic import CalculatorEngine, calculate, format_result


# ---------- calculate() ----------
def test_addition():
    assert calculate(2, "+", 3) == 5

def test_subtraction():
    assert calculate(10, "-", 4) == 6

def test_multiplication():
    assert calculate(5, "*", 10) == 50

def test_divide():
    assert calculate(3, "/", 2) == 1.5

def test_division_by_zero():
    with pytest.raises(ValueError):
        calculate(10, "/", 0)

def test_unknown_operator():
    with pytest.raises(ValueError):
        calculate(10, "%", 2)

def test_negative_numbers():
    assert calculate(-5, "+", 2) == -3

def test_decimal_result():
    assert calculate(5, "/", 2) == 2.5

def test_float_rounding_problem():
    assert calculate(0.1, "+", 0.2) == pytest.approx(0.3)


# ---------- format_result() ----------
def test_format_whole_number():
    assert format_result(8.0) == "8"

def test_format_decimal():
    assert format_result(2.5) == "2.5"

def test_format_float_noise():
    assert format_result(0.1 + 0.2) == "0.3"

def test_format_negative_zero():
    assert format_result(-0.0) == "0"

def test_format_infinity():
    with pytest.raises(ValueError):
        format_result(math.inf)


# ---------- CalculatorEngine (simulates button presses) ----------
def press(keys):
    engine = CalculatorEngine()
    for key in keys:
        engine.press(key)
    return engine.display

def test_simple_sum():
    assert press("7+8=") == "15"

def test_negative_result():
    assert press("5-8=") == "-3"

def test_chaining_gives_correct_total():          # Bug 1
    assert press("2+3+4=") == "9"

def test_chaining_shows_running_total():
    assert press("2+3+") == "5"

def test_error_after_division_by_zero():          # Bug 2
    assert press("5/0=") == "Error"

def test_operator_ignored_after_error():
    assert press("5/0=+3=") == "3"

def test_equals_twice_does_not_repeat():          # Bug 3
    assert press("2+3==") == "5"

def test_float_noise_hidden():                    # Bug 4
    assert press(".1+.2=") == "0.3"

def test_whole_result_has_no_decimal_point():
    assert press("5+3=") == "8"

def test_second_decimal_point_ignored():
    assert press("1.2.3") == "1.23"

def test_leading_decimal_point():
    assert press(".5") == "0.5"

def test_no_leading_zeros():
    assert press("007") == "7"

def test_operator_pressed_twice_uses_last():
    assert press("5+*3=") == "15"

def test_leading_operator_ignored():
    assert press("+5=") == "5"

def test_equals_with_nothing_typed():
    assert press("=") == ""

def test_equals_right_after_operator_ignored():
    assert press("5+=") == "5"

def test_clear_resets_everything():
    assert press("5+3C") == ""
    assert press("5+3C4=") == "4"

def test_continue_after_result():
    assert press("2+3=*4=") == "20"

def test_start_new_number_after_result():
    assert press("2+3=7") == "7"
