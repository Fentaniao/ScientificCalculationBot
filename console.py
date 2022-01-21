import cqdealmsg
import cqsym

from flask import Flask, request
from json import loads

bot_server = Flask(__name__)


@bot_server.route('/api/message', methods=['POST'])
# 路径是你在酷Q配置文件里自定义的
def server():
    data = request.get_data().decode('utf-8')
    data = loads(data)
    print(data)

    user_id = data.get('user_id')
    group_id = data.get('group_id')
    discuss_id = data.get('discuss_id')
    nickname = data['sender'].get('nickname')
    message = data['message'][0]['data'].get('text')
    print('来自QQ:{},昵称:{} 的信息:\n{}'.format(user_id, nickname, message))

    message = cqdealmsg.msg_format(message)
    if message.startswith('sympy'):
        message = message[7:]
        cqsym.deal(user_id, group_id, discuss_id, nickname, message)
    else:
        cqdealmsg.deal(user_id, group_id, discuss_id, nickname, message)

    return ''


if __name__ == '__main__':
    bot_server.run(port=5701)
    # 端口也是你在酷Q配置文件里自定义的
