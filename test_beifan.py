from random import randint

import allure


def test_beifan():
    num = randint(1, 5)
    assert 1 == num

@allure.epic("码尚教育自动化测试项目")
@allure.feature("商品管理模块")
@allure.story("商品管理接口")
@allure.title("商品创建用例-成功")
def test_api():
    pass


@allure.epic("码尚教育自动化测试项目")
@allure.feature("商品管理模块")
@allure.story("商品管理UI")
@allure.title("商品管理UI")
def test_web():
    pass