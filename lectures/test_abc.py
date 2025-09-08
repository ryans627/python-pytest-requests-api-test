import time

import pytest

# # 谨慎使用fixture参数化
# @pytest.fixture(params=[1,2,3])
# def beifan():
#     print("测试执行前执行", time.time())
#     yield
#     print("测试执行后执行", time.time())


@pytest.fixture(autouse=True)
def beifan():
    print("测试执行前执行", time.time())
    yield
    print("测试执行后执行", time.time())

# # 冒名顶替
# @pytest.fixture(autouse=True,name="beifan")
# def beifan_003():
#     print("测试执行前执行", time.time())

# name参数实现冒名顶替
@pytest.fixture(autouse=True,name="beifan")
def beifan_004():
    print("测试执行前执行004", time.time())


def test_abc(beifan):
    print(123)