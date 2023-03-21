# import openpyxl
#
# #创建excel文件
# wb = openpyxl.workbook()
#
# #指定操作的默认sheet页
# sheet = wb.active()
#
#
# sheet.title = "年龄表"
#
#
# sheet["A1"] = "name"
# sheet["B1"] = "age"
#
# sheet["A2"] = "张三"
# sheet["B2"] = "18"
#
# wb.save("个人信息表.xlsx")


import requests


# # 账号添加
# def add_uesr(url,add_data, token):
#     r = requests.post(url=url, json=add_data, headers = {"token":token})
#     return r.json()
#
#
#
#
# a = add_uesr("https://wpzlzp1.zhihuihedao.cn/smart_pipe/user/user_manage/add",
# { "loginName": "15552633690", "userContact": "15552633690", "userName": "测试账号",
# "userPwd": "", "avatar": "","isEnable": 0,"munit": 11,"isAlone": 0,"endTime": "","roleType": 3
# },"XFg7TjmczFZyyuD8syhsEfj130H7AGK//SBiZM1bCwk=")
# print(a)

