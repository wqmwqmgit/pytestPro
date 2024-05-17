import jsonpath
import pytest
import requests

from common.csv_util import readCsv
from common.request_util import RequestUtil
from common.yaml_util import write_yaml, read_yaml, read_testdata



class TestUserManage:
    @pytest.mark.smoke
    # @pytest.mark.parametrize('casedata',read_testdata('./testcase/test_getToken.yaml'))
    @pytest.mark.parametrize('casedata',readCsv('./csv/datadrive.csv'))
    def test_getToken(self,casedata):
        print(casedata)
        print(type(casedata))
        url = casedata['url']
        print(url)
        method = casedata['method']
        grant_type = casedata['grant_type']
        appid = casedata['appid']
        secret = casedata['secret']
        assertCode = casedata['assertCode']

        datas = {
            'grant_type': grant_type,
            'appid': appid,
            'secret': secret
        }

        res = RequestUtil().all_send_request(method=method,url=url, params=datas)
        result = res.json()
        if "access_token" in res.text:
            access_token = jsonpath.jsonpath(result, '$.access_token')
            # 获取access_token，写入到yaml文件
            dict = {'access_token': access_token[0]}
            write_yaml(dict)
            assert assertCode == '200'
        else:
            assert assertCode == '41001'

