import time


class Test:
    # 前置：在每个用例执行之前执行
    def setup_method(self):
        print("用例开始执行", time.time())

    # 后置：在每个用例执行之后执行
    def teardown_method(self):
        print('用例结束执行', time.time())

    # 前置：在每个测试类执行之前
    def setup_class(self):
        print("测试类开始执行", time.time())

    # 后置：在每个测试类执行之后
    def teardown_class(self):
        print('测试类结束执行', time.time())

    def test_a(self):
        assert 1 == 1

    def test_b(self):
        assert 1 == 2