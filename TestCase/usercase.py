import unittest
from API.User_api import UserApi
from common.sql import get_sql

from common.get_token import get_token
token = get_token()


class User_case(unittest.TestCase):

    uid = None

    def setUp(self) -> None:
        self.user_api = UserApi()

    def tearDown(self) -> None:
        pass


    # 添加账号
    def test01_add_user_ok(self):
        response = self.user_api.add_uesr({
            "loginName": "13552601690",
            "userContact": "13552601690",
            "userName": "周一",
            "userPwd": "",
            "avatar": "",
            "isEnable": 0,
            "munit": 11,
            "isAlone": 0,
            "endTime": "",
            "roleType": 3
        }, token)
        print(response, type(response))
        self.assertEqual("插入成功", response.get("message"))

    # 查询账号列表
    def test02_sel_user_ok(self):
        res = self.user_api.sel_uesr({"pageNum": 1, "pageSize": 10}, token)
        print(res, type(res))
        # # 提取出新增用户的id
        User_case.uid = res.get("data").get("list")[0].get("userId")
        print(User_case.uid)

    # 修改账号名称参数
    def test03_update_user_ok(self, user_id=None):
        res = self.user_api.update_uesr({
            "userId": User_case.uid,
            "loginName": "13552601697",
            "userName": "周五",
            "userContact": "15552633691",
            "useType": 1,
            "isEnable": 0,
            "munit": 11,
            "roleType": 3,
            "roleTypeStr": "运维公司运维人员",
            "isAlone": 0,
        },token)
        print(res)
        #断言
        self.assertEqual("更新成功",res.get("message"))


    #删除账号
    def test05_del_user_ok(self):
        res =self.user_api.delete_uesr({"ids":[User_case.uid]},token)
        print(res)
        #断言
        self.assertEqual("删除成功",res.get("message"))



