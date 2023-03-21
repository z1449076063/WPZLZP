import unittest
from path import BASE_DIR
import time

from TestCase.logincase import Login_case
from TestCase.usercase import User_case
from TestCase.usercase_CSH import User_case_CSH
from lib.HTMLTestRunner_PY3 import HTMLTestRunner

# 组装测试套件
suite = unittest.TestSuite()
# 登录的用例
suite.addTest(unittest.makeSuite(Login_case))
# 账号管理的用例
suite.addTest(unittest.makeSuite(User_case))
# 账号管理新增的参数化用例
suite.addTest(unittest.makeSuite(User_case_CSH))

# 获取当前的时间
now = time.strftime("%Y%m%d %H%M%S", time.localtime())

# 指定报告生成的位置
report = BASE_DIR + f'/report/{now} report.html'
print(report)

with open(report, "wb") as f:
    runner = HTMLTestRunner(stream=f, title="自动化测试报告")
    runner.run(suite)


