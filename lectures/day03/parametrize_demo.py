import pytest

from commons.yaml_utils import YamlUtil


@pytest.mark.parametrize(
    "data",
    YamlUtil("../../data/ddt_plus.yaml").read()['values'],  # 使用从文件读取的方式代替在代码中直接写的方式
    ids=YamlUtil("../../data/ddt_plus.yaml").read()['ids']
)
def test_ddt(data):
    a, b, c = data
    _c = a + b  # 实际结果
    assert _c == c  # 预期结果
