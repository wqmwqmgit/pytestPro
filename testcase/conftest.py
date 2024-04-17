
import pytest

from common.yaml_util import clear_yaml


# from common.yaml_util import clear_yaml


#fixture固件
@pytest.fixture(scope='class',autouse=False,params=[['baili','baili123'],['beifan','beifan123']])
def exe_sql(request):
    print('查询sql语句')
    yield request.param
    print('关闭连接')

@pytest.fixture(scope='session',autouse=True)
def clearyaml():
    clear_yaml()