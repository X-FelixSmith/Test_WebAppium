# from calculator import
# from class_demo.calculator import Calculator


# def aaa(a, b):
#     return a + b
import pytest

from calculator import Calculator


class TestCal:
    def setup_class(self):
        print("\n类级别的 setup")

    def teardown_class(self):
        print("类级别的 teardown")

    def setup(self):
        print("准备工作setup")

    def teardown(self):
        print("\n结束工作teardown")

    def test_add(self):
        calc = Calculator()
        assert calc.add(1, 1) == 2

    def test_add1(self):
        calc = Calculator()
        assert calc.add(1, 1) == 2

def add01(a,b):
    return a+b
@pytest.mark.parametrize("a,b,expect",[[1,2,3],[0.1,0.2,0.3],[-1,-2,-3]],ids=['int1','float1','int2'])
def test_add01(a,b,expect):
    assert add01(a,b) == expect