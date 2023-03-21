import pymysql


def get_sql(host, port, username, password, db, s):
    """

    :param host: 连接服务器的地址
    :param port: 端口号
    :param username: 用户名
    :param password: 密码
    :param db: 数据库的库名
    :param s: 需要的sql语句
    :return:
    """
    # 建立数据库的连接
    conn = pymysql.connect(host=host, port=port, user=username, password=password, database=db)

    # 创建游标
    cur = conn.cursor()

    # 传入sql
    cur.execute(s)

    # 控制台输出sql运行结果
    return cur.execute(s)
    # print(cur.execute(s))

    # 关闭连接
    conn.close()


if __name__ == '__main__':
    host = "122.9.71.74"
    port = 61307
    username = "root"
    password = "jwsz++321."
    db = "jw_wpz_smart_pipe"
    s = 'SELECT * FROM `water_well` where well_name LIKE "%YSJ00%" and is_delete = 0'
    a = get_sql(host, port, username, password, db, s)
