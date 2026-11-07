def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a: float, b: float) -> float:
    try:
        result = a**b
    except (ZeroDivisionError, OverflowError):
        raise ValueError("Cannot compute this power")
    if isinstance(result, complex):
        raise ValueError("Result is not a real number")
    return result