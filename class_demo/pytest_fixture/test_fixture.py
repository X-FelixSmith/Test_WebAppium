import pytest


@pytest.fixture()
def login():
    print("\nlogin")
    token = '123abc'
    yield token
    print("登录结束")


def test_cart(login):
    print("cart")

def test_order(login):
    print("order")
    print(f"my token = {login}")