"""
Тесты для службы доставки. Чтобы они работали.
Необходимо удалить ввод с клавиатуры.
"""
from delivery_service import check_platform

def test_delivery():
    res = check_platform(3, sorted[3, 2, 2, 1])
    assert res == 3

def test_delivery1():
    res = check_platform(5, sorted[1, 3, 4, 2])
    assert res == 2

def test_delivery2():
    res = check_platform(100, sorted[20, 30, 40, 50, 55, 70, 80])
    assert res == 4

def test_delivery3():
    res = check_platform(100, sorted[30, 50, 70, 80])
    assert res == 3

def test_delivery4():
    res = check_platform(100, sorted[50, 50, 50, 50])
    assert res == 2

def test_delivery5():
    res = check_platform(3, sorted[1, 2])
    assert res == 1

def test_delivery6():
    res = check_platform(10, sorted[1, 1, 1, 1, 1, 1])
    assert res == 3