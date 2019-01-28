# 信息双向适配
import json

from face_rec import recognition_fea
from forServer import *

"""
选择指令
"""


def invoke(fun, *msg):
    if (len(msg) == 0):
        return fun
    else:
        return fun(msg[0])


"""
输入json，信息转换成对应指令
"""


def handle(msg):
    obj = json.loads(msg)

    if obj['action'] == "newUser":
        fun = create_new_user
    elif obj == "rec":
        fun = recognition_fea
    try:
        invoke(fun, obj['msg'])

    except Exception as Argument:
        return handle_error(Argument)
    return {"code":1}


"""
异常处理
"""


def handle_error(msg):
    res = {'code': -1, 'msg': msg}
    return res


if __name__ == '__main__':
    msg={"action":"newUser","msg":"4.jpg"};
    msg=handle(json.dumps(msg))
    print(msg)
