import pytest
import os

pytest.main() # 启动框架=加载插件+执行用例=得到allure数据
os.system("allure generate ./temps -o ./reports --clean")