from function.getvoice import *


# 发送私聊/群聊/讨论组消息（强功能）
def send_msg(message_type, id, message):
    data = {
        message_type + '_id': id,
        'message': message,
        'auto_escape': False
    }

    url_suffix = '/send_msg'
    requests.post('http://127.0.0.1:5700' + url_suffix, data=data)
    return 1


# 根据消息ID撤回消息
def delete_msg(message_id):
    data = {
        'message_id': message_id
    }
    url_suffix = '/delete_msg'
    return requests.post('http://127.0.0.1:5700' + url_suffix, data=data)


# 向QQ好友发送名片赞
def send_like(user_id, times=10):
    data = {
        'user_id': user_id,
        'times': times
    }
    url_suffix = '/send_like'
    return requests.post('http://127.0.0.1:5700' + url_suffix, data=data)


# Q群管理group_manage下的group_函数族
class group_manage:
    def __init__(self, group_id):
        self.group_id = group_id
        self.data = {
            'group_id': group_id
        }

    # 在群里发送语音信息
    def group_send_record(self, text):
        api_url = 'http://127.0.0.1:5700/send_msg'
        self.data['msg_type'] = 'group'
        self.data['message'] = '[CQ:record,file=base64://{}]'.format(tts(text))
        requests.post(api_url, data=self.data)

    # 开关全员禁言
    def group_whole_ban(self, enable=False):
        self.data['enable'] = enable

        url_suffix = '/set_group_whole_ban'
        return requests.post('http://127.0.0.1:5700' + url_suffix, data=self.data)

    # 开关匿名聊天
    def group_anonymous(self, enable=False):
        self.data['enable'] = enable

        url_suffix = '/set_group_anonymous'
        return requests.post('http://127.0.0.1:5700' + url_suffix, data=self.data)

    # 设置管理员
    def group_admin(self, user_id, enable):
        self.data['user_id'] = user_id
        self.data['enable'] = enable

        url_suffix = '/set_group_whole_ban'
        return requests.post('http://127.0.0.1:5700' + url_suffix, data=self.data)

    # 设置群名片
    def group_card(self, user_id, card):
        self.data['user_id'] = user_id
        self.data['card'] = card

        url_suffix = '/set_group_card'
        return requests.post('http://127.0.0.1:5700' + url_suffix, data=self.data)

    # 踢掉一个人
    def group_kick(self, user_id, reject_add_request=False):
        self.data['user_id'] = user_id
        self.data['reject_add_request'] = reject_add_request

        url_suffix = '/set_group_kick'
        return requests.post('http://127.0.0.1:5700' + url_suffix, data=self.data)

    # 禁言单人用户
    def group_ban(self, user_id, duration):
        self.data['user_id'] = user_id
        self.data['duration'] = duration

        url_suffix = '/set_group_ban'
        return requests.post('http://127.0.0.1:5700' + url_suffix, data=self.data)

    # 禁言匿名用户
    def group_anonymous_ban(self, id, duration):
        self.data['id'] = id
        self.data['duration'] = duration

        url_suffix = '/set_group_ban'
        return requests.post('http://127.0.0.1:5700' + url_suffix, data=self.data)


# 获取登录号信息
def get_login():
    url_suffix = '/get_login_info'
    abc = requests.post('http://127.0.0.1:5700' + url_suffix)

    return print(abc)


# 获取陌生人信息
def get_stranger(user_id, no_cache=False):
    data = {
        'user_id': user_id,
        'no_cache': no_cache
    }

    url_suffix = '/get_stranger_info'
    return requests.post('http://127.0.0.1:5700' + url_suffix, data=data)


# 获取get_group下的get_group函数族
class get_group:
    def __init__(self, group_id):
        self.group_id = group_id
        self.data = {
            'group_id': group_id
        }

    # 获取群信息
    def get_group_info(self, no_cache=False):
        self.data['no_cache'] = no_cache

        url_suffix = '/get_group_info'
        re = requests.post('http://127.0.0.1:5700' + url_suffix, data=self.data)
        print(re.text)

        re_dict = re.json()  # 将json转换为字典
        re_data = re_dict['data']
        group_id = re_data['group_id']
        group_name = re_data['group_name']
        max_member_count = re_data['max_member_count']
        member_count = re_data['member_count']
        info = '这是一个名叫“%s”的群，Q群号为%s，群人数为%d/%d人' % (group_name, group_id, member_count, max_member_count)
        send_msg('group', self.group_id, info)
        return re_data
