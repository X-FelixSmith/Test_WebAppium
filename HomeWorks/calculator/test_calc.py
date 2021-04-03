import pytest
import yaml

from calculator import Calculator


class TestCalc():
    with open("./calc_data.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    print(data)

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    # 整数 加法
    @pytest.mark.parametrize("a,b,expect", data["add_int"]["datas"], ids=data["add_int"]["ids"])
    def test_add_int(self, a, b, expect):
        print("计算整数加法")
        calc = Calculator()
        assert calc.add(a, b) == expect

    # 浮点数 加法
    @pytest.mark.parametrize("a,b,expect", data["add_float"]["datas"], ids=data["add_float"]["ids"])
    def test_add_float(self,a,b,expect):
        calc = Calculator()
        print("计算浮点数加法")
        assert round(calc.add(a, b),2) == expect

    # 整数除法
    @pytest.mark.parametrize("a,b,expect", data["div_datas"]["datas"], ids=data["div_datas"]["ids"])
    def test_division(self, a, b, expect):
        calc = Calculator()
        print("计算整数除法")
        try:
            assert calc.division(a, b) == expect

        except ZeroDivisionError as e:
            print("除数为零")
