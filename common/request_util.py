import requests


class RequestUtil:
    session = requests.session()
    # 统一请求封装
    def all_send_request(self,**kwargs):
       res = RequestUtil.session.request(**kwargs)
       print(res.text)
       print(res.status_code)
       return res
