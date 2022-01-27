# -*- coding: utf-8 -*-
# 腾讯云人脸识别
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的 client models。
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.iai.v20180301 import iai_client, models
import base64

def get_json(img_dir):
    with open(img_dir, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        base64_code = base64_data.decode()
    try:
        # 实例化一个客户端配置对象，可以指定超时时间等配置
        clientProfile = ClientProfile()
        clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法
        # 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey
        cred = credential.Credential(secretId, secretKey)
        client = iai_client.IaiClient(cred, "ap-guangzhou", clientProfile)
        # 实例化一个请求对象
        req = models.DetectFaceRequest()

        # 人脸检测参数
        req.MaxFaceNum = 1
        req.Image = base64_code
        req.NeedFaceAttributes = 1
        req.NeedQualityDetection = 0

        # 通过 client 对象调用想要访问的接口，需要传入请求对象
        resp = client.DetectFace(req)
        # 输出 JSON 格式的字符串回包
        json_data = resp.to_json_string()

        return json_data

    except TencentCloudSDKException as err:
        print(err)
        return None

secretId = ' '
secretKey = ''
img_dir = ''
json_data = get_json(img_dir)