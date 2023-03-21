import requests
import json

def get_token():
    url = "https://wpzlzp1.zhihuihedao.cn/smart_pipe/user/open/login"
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    data = {"account": "13885598575", "password": "123456"}
    response = requests.post(url,headers=headers,data=json.dumps(data))
    token = response.json().get("data").get("token")
    return token

if __name__ == '__main__':
    print(get_token())