import jsonpath
import pytest
import requests
from common.request_util import RequestUtil
from common.yaml_util import write_yaml, read_yaml, read_testdata


class TestUserManage:
    @pytest.mark.smoke
    @pytest.mark.parametrize('casedata',read_testdata('./testcase/test_getToken.yaml'))
    def test_getToken(self,casedata):
        print(casedata)
        url = casedata['request']['url']
        dates = casedata['request']['params']
        method = casedata['request']['method']
        # dates = {
        #     'grant_type': 'client_credential',
        #     'appid': 'wxaa666e3ee0f3cf54',
        #     'secret': 'd16004d19f8a85d02b1d9c5e93f06bc2'
        # }
        res = RequestUtil().all_send_request(method=method,url=url, params=dates)
        result = res.json()
        if "access_token" in res.text:
            access_token = jsonpath.jsonpath(result, '$.access_token')
            # 获取access_token，写入到yaml文件
            dict = {'access_token': access_token[0]}
            write_yaml(dict)


    @pytest.mark.usermanager
    def test_getUserList(self):
        url = 'https://api.weixin.qq.com/cgi-bin/user/get?'
        dates = {
            'access_token': read_yaml('access_token'),
            'next_openid': ''
        }
        res = RequestUtil().all_send_request(method='get',url=url, params=dates)

    def test_setUserName(self):
        url = 'https://api.weixin.qq.com/cgi-bin/user/info/updateremark?access_token='+read_yaml('access_token')
        dates = {
            # 'access_token': TestUserManage.access_token,
            "openid": "okOFz6XQ8E7id1i39eHm5chr2WLs",
            "remark": "wqmTest"
        }
        RequestUtil().all_send_request(method='post',url=url,json=dates)

    def test_getUserInfo(self):
        url = 'https://api.weixin.qq.com/cgi-bin/user/info?'
        dates = {
            'access_token':read_yaml('access_token'),
            'openid':'okOFz6XQ8E7id1i39eHm5chr2WLs',
            'lang':'zh_CN'
        }
        RequestUtil().all_send_request(method='get', url=url, params=dates)
# if __name__ == '__main__':
#     TestUserManage().test_getToken()
#     TestUserManage().test_getUserList()

