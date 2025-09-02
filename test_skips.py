import pytest


def test_a():
    assert 1 == 1

# 有条件跳过
@pytest.mark.skipif(1 != 1, reason="当1等于1的时候跳过")
def test_b():
    assert 1 == 2

# 无条件跳过
@pytest.mark.skip
def test_c():
    assert 3 == 3

@pytest.mark.xfail
def test_d():
    assert 1 == 1 # XPASS: 虽然用例没报错，可是我们预期它失败，它改变了我们的预期

@pytest.mark.xfail
def test_e():
    assert 1 == 2 # XFAIL