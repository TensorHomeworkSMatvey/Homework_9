import fib

def test_1():
    assert fib.f(1) == 1

def test_2():
    assert fib.f(2) == 1

def test_minus_3():
    assert fib.f(-3) == "Число меньше 1"

def test_8():
    assert fib.f(8) == 21