import unittest

import read_file
from API.User_api import UserApi
from parameterized import parameterized

from common.get_token import get_token

token = get_token()


class User_case_CSH(unittest.TestCase):
    uid = None

    def setUp(self) -> None:
        self.user_api = UserApi()

    def tearDown(self) -> None:
        pass

    # 添加账号
    # 用例的参数化
    @parameterized.expand(read_file.read_file())
    def test01_add_user_ok(self, add_data, message):
        response = self.user_api.add_uesr(add_data, token)
        print(response, type(response))
        self.assertEqual(message, response.get("message"))
