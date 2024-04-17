import pytest

from common.request_util import RequestUtil
from common.yaml_util import read_yaml


class TestBasicMessage:
    def test_MroadcastMessage(self):
        url = 'https://api.weixin.qq.com/cgi-bin/message/mass/sendall?access_token='+read_yaml('access_token')
        print(url)
        dates = {
            "filter": {
                "is_to_all": True
            },
            "text": {
                "content": "wqmwqmwqm"
            },
            "msgtype": "text"
        }
        res = RequestUtil().all_send_request(method='post',url=url, json=dates)
