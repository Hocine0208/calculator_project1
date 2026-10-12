"""Calculator logic: no GUI code in this file, so pytest can test everything."""

import math


def calculate(a, op, b):
    """Apply one operator to two numbers."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Unknown operator")


def format_result(value):
    """Turn a number into display text: 8.0 -> '8', 0.30000000000000004 -> '0.3'."""
    if not math.isfinite(value):
        raise ValueError("Result is too large")
    value = round(value, 10)
    if value == int(value):
        return str(int(value))
    return str(value)


class CalculatorEngine:
    """Holds the calculator state. The UI sends it button labels and shows .display."""

    OPERATORS = ("+", "-", "*", "/")

    def __init__(self):
        self.reset()

    def reset(self):
        self.display = ""
        self.first_number = None
        self.operator = None
        self.start_new_number = True

    def press(self, label):
        """Handle one button press and return the text the display should show."""
        if label.isdigit():
            self._digit(label)
        elif label == ".":
            self._decimal()
        elif label in self.OPERATORS:
            self._operator(label)
        elif label == "=":
            self._equals()
        elif label == "C":
            self.reset()
        return self.display

    # ---- helpers ----
    def _current_number(self):
        """The display as a float, or None if it is empty or says 'Error'."""
        try:
            return float(self.display)
        except ValueError:
            return None

    def _error(self):
        self.display = "Error"
        self.first_number = None
        self.operator = None
        self.start_new_number = True

    # ---- button handlers ----
    def _digit(self, digit):
        if self.start_new_number or self.display == "0":
            self.display = digit
        else:
            self.display += digit
        self.start_new_number = False

    def _decimal(self):
        if self.start_new_number:
            self.display = "0."
            self.start_new_number = False
        elif "." not in self.display:
            self.display += "."

    def _operator(self, op):
        number = self._current_number()
        if number is None:
            return  # nothing valid to work with (empty display or "Error")

        # A second number was typed: finish the pending operation first (chaining).
        if self.operator is not None and not self.start_new_number:
            try:
                number = calculate(self.first_number, self.operator, number)
                self.display = format_result(number)
            except ValueError:
                self._error()
                return

        self.first_number = number
        self.operator = op
        self.start_new_number = True

    def _equals(self):
        number = self._current_number()
        if self.operator is None or self.start_new_number or number is None:
            return  # no complete operation to compute

        try:
            result = calculate(self.first_number, self.operator, number)
            self.display = format_result(result)
        except ValueError:
            self._error()
            return

        self.first_number = None
        self.operator = None
        self.start_new_number = True
