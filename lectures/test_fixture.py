import time

import pytest


@pytest.fixture()
def beifan():
    # yield之前 => 前置操作
    print("用例开始执行", time.time())
    yield
    # yield之后 => 后置操作
    print("用例结束执行", time.time())

@pytest.fixture(scope="session")
def beifan_class():
    # yield之前 => 前置操作
    print("测试类开始执行", time.time())
    yield
    # yield之后 => 后置操作
    print("测试类结束执行", time.time())

class Test:
    # 声明使用了哪个fixture
    def test_a(self, beifan):
        assert 1 == 1

    def test_b(self):
        assert 1 == 2