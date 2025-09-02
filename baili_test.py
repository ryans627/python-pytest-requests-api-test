import pytest


@pytest.mark.smoke
def test_baili():
    assert 1 == 1

@pytest.mark.web
def test_a():
    pass

@pytest.mark.api
@pytest.mark.order(2)
def test_b():
    pass

@pytest.mark.ut
@pytest.mark.api
@pytest.mark.order(1)
def test_c():
    pass
