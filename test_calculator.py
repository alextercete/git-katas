from calculator import Calculator

def test_sum():
    calculator = Calculator()
    assert calculator.sum(1, 2) == 3

def test_subtraction():
    calculator = Calculator()
    assert calculator.subtract(5, 2) == 3
