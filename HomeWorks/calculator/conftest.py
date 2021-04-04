import pytest
import yaml

from calculator import Calculator


@pytest.fixture()
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


def get_datas():
    with open("./calc_data.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data


def get_data_add_int():
    return get_datas()['add_int']['datas'], get_datas()['add_int']['ids']


def get_data_add_float():
    return get_datas()['add_float']['datas'], get_datas()['add_float']['ids']


def get_data_div():
    return get_datas()['div_datas']['datas'], get_datas()['div_datas']['ids']


@pytest.fixture(params=get_data_add_int()[0], ids=get_data_add_int()[1])
def data_add_int(request):
    return request.param


@pytest.fixture(params=get_data_add_float()[0], ids=get_data_add_float()[1])
def data_add_float(request):
    return request.param


@pytest.fixture(params=get_data_div()[0], ids=get_data_div()[1])
def data_div(request):
    return request.param
