# 实用程序

[TOC]

## 科学百科

<p>
    <img alt="Wolfram" src="https://img.shields.io/badge/-Wolfram-3572A5?style=flat&logo=Wolfram&logoColor=white" />
    <img alt="Wolfram Language" src="https://img.shields.io/badge/-Wolfram_Language-3572A5?style=flat&logo=WolframLanguage&logoColor=white" />
</p>

#### 描述

调用Wolfram API实现通过Wolfram搜索引擎进行科学百科。

#### `easy_res`简单结果

##### 参数

| 参数    | 数据类型 | 默认值 | 说明 |
| ------- | -------- | ------ | ---- |
| `query` | 字符串   | -      | 问题 |

##### 响应

通过文字消息返回回答的结果

#### `short_answers`简短回答

##### 参数

| 参数    | 数据类型 | 默认值 | 说明 |
| ------- | -------- | ------ | ---- |
| `query` | 字符串   | -      | 问题 |

##### 响应

通过文字消息返回回答的结果

#### `conversational`会话式回答

##### 参数

| 参数    | 数据类型 | 默认值 | 说明 |
| ------- | -------- | ------ | ---- |
| `query` | 字符串   | -      | 问题 |
| `user_id` | 数   | -      | 用户号码 |

##### 响应

通过文字消息返回回答的结果

## 发送语音

<p>
    <img alt="Alibaba Cloud" src="https://img.shields.io/badge/-Alibaba_Cloud-3572A5?style=flat&logo=AlibabaCloud&logoColor=white" />
</p>

#### 描述

调用阿里云API实现语音消息。

#### `group_send_record`在群里发送语音信息

##### 参数

| 参数    | 数据类型 | 默认值 | 说明 |
| ------- | -------- | ------ | ---- |
| `text` | 字符串   | -      | 文本 |

##### 响应

通过文字消息返回回答的结果

## 实验性功能(Beta)

### 人脸识别


<p>
    <img alt="Tecent Cloud" src="https://img.shields.io/badge/-Tecent_Cloud-3572A5?style=flat&logo=tencentqq&logoColor=white" />
</p>
#### 描述

调用腾讯云API实现人脸识别。

### 拼写纠正

### 单词统计

##### 输入

输入待统计的字符串

##### 处理

对输入的文章进行预处理，全部化为小写，删去无关字符，最后拆分得到单词列表

统计单词在单词列表中的出现次数，生成以单词为键，单词出现次数为值的字典,并对字典进行处理

由上一步的字典，生成以单词出现次数为键，对应单词放进列表中为值的新字典

分别按照出现次数和单词在字母表里的顺序进行排序

##### 响应

通过文字消息返回回答的结果