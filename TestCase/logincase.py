# 导入测试用例的组装套件
import unittest
# 导入登录接口
from API.Login_api import LoginApi


class Login_case(unittest.TestCase):
    def setUp(self) -> None:
        self.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    def test01_login_ok(self):
        # 输入正确的用户名和密码
        response = self.login_api.login({"account": "13885598575", "password": "123456"})
        print(response.json())
        self.assertEqual("登录成功", response.json().get("message"))

    def test02_account_empty(self):
        # 用户名为空
        response = self.login_api.login({"account": "", "password": "123456"})
        print(response.json())
        self.assertEqual("参数错误,请输入登录名", response.json().get("message"))

    def test03_account_error(self):
        # 用户名错误
        response = self.login_api.login({"account": "13885858789", "password": "123456"})
        print(response.json())
        self.assertEqual("用户不存在，请先注册！", response.json().get("message"))
