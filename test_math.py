# test_math.py
from math import Math

def test_absolute_positive():
    m = Math()
    assert m.absolute(5) == 5

def test_absolute_negative():
    m = Math()
    assert m.absolute(-5) == 5

def test_absolute_zero():
    m = Math()
    assert m.absolute(0) == 0


def test_sign_positive():
    m = Math()
    assert m.sign(5) == 1

def test_sign_negative():
    m = Math()
    assert m.sign(-5) == -1

def test_sign_zero():
    m = Math()
    assert m.sign(0) == 0
