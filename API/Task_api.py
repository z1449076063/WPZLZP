import requests
from common.yuming import url1
import json


class TaskApi:
    def __init__(self):
        self.url = url1 + "/smart_pipe/pc/task/add_task"

    # 任务新增接口
    def add_task(self, add_data, token):
        res = requests.post(url=self.url, json=add_data,
                            headers={"token": token})

        # r = res.json()
        return res


if __name__ == '__main__':
    add_data = {"taskCategory": 3, "implementIds": [5469], "taskName": "临时任务测试", "communityId": 19,
                "implementType": 20, "itemsReqList": [{"index": 0, "itemContent": "测试1", "conformityFlag": 1}]}
    token = "xV8V+HGUNmtfkG+FajsR/13S+MPCP9/m9AOzty4CUkM="
    t = TaskApi()
    a = t.add_task(add_data, token)
    print(a.json())
