import json
from path import BASE_DIR


# 封装读取文件的方法
def read_file(name):
    file = BASE_DIR + fr"/file/{name}.json"
    test_list = []
    with open(file, encoding="utf-8") as f:
        data = json.load(f)
        for i in data:
            add_data = i.get("add_data")
            message = i.get("message")

            test_list.append((add_data, message))

        print(test_list,type(test_list))

#
#
# if __name__ == '__main__':
#     print(read_file("add_user"))
