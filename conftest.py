import time

import pytest


@pytest.fixture(autouse=True)
def beifan():
    print("测试执行前执行", time.time())
    yield
    print("测试执行后执行", time.time())