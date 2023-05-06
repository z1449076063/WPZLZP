import requests

from common.yuming import url1


class UserApi:
    try:
        def __init__(self):
            self.url_add = url1 + "/smart_pipe/user/user_manage/add"
            self.url_sel = url1 + "/smart_pipe/user/user_manage/list"
            self.url_update = url1 + "/smart_pipe/user/user_manage/update"
            self.url_delete = url1 + "/smart_pipe/user/user_manage/delete"

        # 账号添加
        def add_uesr(self, add_data, token):
            r = requests.post(url=self.url_add, json=add_data, headers={"token": token})
            return r.json()

        # 账号查询
        def sel_uesr(self, sel_data, token):
            r = requests.post(url=self.url_sel, json=sel_data, headers={"token": token})
            return r.json()

        # 账号修改
        def update_uesr(self, update_data, token):
            r = requests.post(url=self.url_update, json=update_data, headers={"token": token})
            return r.json()

        # 账号删除
        def delete_uesr(self, delete_data, token):
            r = requests.post(url=self.url_delete, json=delete_data, headers={"token": token})
            return r.json()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    add_data = {
                "loginName": "17552633697",
                "userContact": "17552633697",
                "userName": "测试账号",
                "userPwd": "",
                "avatar": "",
                "isEnable": 0,
                "munit": 11,
                "isAlone": 0,
                "endTime": "",
                "roleType": 3
            }

    # sel_data = {"pageNum": 1, "pageSize": 10}
    token = "XFg7TjmczFZyyuD8syhsEfj130H7AGK//SBiZM1bCwk="
    r = UserApi()
    print(r.add_uesr(add_data, token))
