import requests


class msg:
    def __init__(self, message_type, id, message):
        self.message_type = message_type
        self.id = id
        self.message = message

    def edit(self):
        data = {
            self.message_type + '_id': self.id,
            'message': self.message,
            'auto_escape': False
        }
        return data

    def send_directly(self):
        data = {
            self.message_type + '_id': self.id,
            'message': self.message,
            'auto_escape': False
        }

        url_suffix = {'user': '/send_private_msg', 'group': '/send_group_msg', 'discuss': '/send_discuss_msg'}
        return requests.post('http://127.0.0.1:5700' + '/send_msg', data=data)

    def withdraw_msg(self, message_id):
        data = {
            'message_id': message_id
        }
        url_suffix = '/delete_msg'
        return requests.post('http://127.0.0.1:5700' + url_suffix, data=data)


def group_ban(id, user_id, duration):
    data = {
        'group_id': id,
        'user_id': user_id,
        'duration': duration
    }
    url_suffix = '/set_group_ban'
    return requests.post('http://127.0.0.1:5700' + url_suffix, data=data)

group_ban(704712560,2854196312,30)

import time

# time.sleep(20)

localtime = time.asctime(time.localtime(time.time()))

data0 = msg('user', 927640917, '同学们好，下面即将接受检阅的是我最新研发的新一代复读机群~\n').edit()
data = msg('user', 927640917, '我是一个可爱的小喵喵~').edit()
data2 = msg('user', 927640917, '我对复读事业有着无穷的热爱~').edit()
data3 = msg('user', 927640917,
            '安好，我的主人\n现在的时间是： ' + str(localtime), ).edit()

data5 = {
    'user_id': 927640917,
    'message': '复读机群检阅完毕',
    'auto_escape': False
}

url_suffix = '/send_msg'
api_url = 'http://127.0.0.1:5700' + url_suffix
# 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700

# r0 = requests.post(api_url, data=data0)
msg('group', 704712560, '同学们好，下面即将接受检阅的是我最新研发的新一代复读机群~\n').send_directly()
i = 1
time.sleep(5)
while i <= 3:
    r = requests.post(api_url, data=data)
    r2 = requests.post(api_url, data=data2)
    r3 = requests.post(api_url, data=data3)

    data4 = {
        'user_id': 927640917,
        'message': '刚刚飞过的是第' + str(i) + '架复读机',
        'auto_escape': False
    }
    r4 = requests.post(api_url, data=data4)
    i += 1
r5 = requests.post(api_url, data=data5)

print(r.text)
