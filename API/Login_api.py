
import requests

from common.yuming import url1


class LoginApi:
    def __init__(self):
        self.url_login = url1 + "/smart_pipe/user/open/login"


    def login(self,login_data):
        return requests.post(url=self.url_login,json =login_data)





if __name__ == "__main__":
    # url = "https://wpzlzp1.zhihuihedao.cn/smart_pipe/user/open/login"
    # headers = {"Content-Type": "application/json;charset=UTF-8"}
    login_data = {"account": "13885598575", "password": "123456"}
    a = LoginApi()
    l = a.login(login_data)
    print(l.json())

