import allure
import pytest
import yaml

from calculator import Calculator

@allure.feature("计算器测试")
class TestCalc():

    # 整数 加法
    @allure.story("整数相加功能")
    def test_add_int(self, get_calc,data_add_int):
        print("计算整数加法")
        assert get_calc.add(data_add_int[0],data_add_int[1]) == data_add_int[2]

    # 浮点数 加法
    @allure.story("浮点数相加功能")
    def test_add_float(self,get_calc,data_add_float):
        print("计算浮点数加法")
        assert round(get_calc.add(data_add_float[0],data_add_float[1]),2) == data_add_float[2]

    # 整数除法
    @allure.story("除法功能")
    def test_division(self, get_calc,data_div):
        print("计算整数除法")
        try:
            assert get_calc.division(data_div[0], data_div[1]) == data_div[2]
        except ZeroDivisionError as e:
            print("除数为零")
