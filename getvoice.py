from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json
import base64
import requests

# 密钥
accessKey = ''
accessSecret = ''
appKey = ''

botServerApi = 'http://127.0.0.1:5700/send_msg'


def get_aliyun_secret():
    client = AcsClient(accessKey, accessSecret, 'cn-shanghai')
    request = CommonRequest()
    request.set_method('POST')
    request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
    request.set_version('2019-02-28')
    request.set_action_name('CreateToken')
    r = client.do_action_with_exception(request)
    r = json.loads(r.decode())
    return r['Token'].get('Id')


def tts(text):
    data = {
        'appkey': appKey,  # 语音合成项目里的appkey
        "text": text,  # 要语音合成的文字
        'token': get_aliyun_secret(),  # 上一步的鉴权秘钥
        'format': 'mp3',  # 合成语音的格式
        "sample_rate": "16000",  # 比特率
        "volume": '100',  # 音量
        "pitch_rate": '-100',  # 语调
        "speech_rate": '-250',  # 语速
        "voice": 'aiwei'  # 发音人 参数详见 https://help.aliyun.com/document_detail/84435.html
    }
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    r = requests.post('https://nls-gateway.cn-shanghai.aliyuncs.com/stream/v1/tts', data=json.dumps(data),
                      headers=header)
    return base64.b64encode(r.content).decode()

# def send_record(group_id,text):
#     api_url = 'http://127.0.0.1:5700/send_msg'
#     data = {
#         'msg_type': 'group',
#         'group_id':group_id,
#         'message':'[CQ:record,file=base64://{}]'.format(tts(text))
#     }
#     requests.post(api_url,data=data)
#
# if __name__ == '__main__':
#     send_record(12345678,'今天天气真不错')
