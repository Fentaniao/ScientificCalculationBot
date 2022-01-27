<p align="center">
 <img width="100px" src="README.assets/logo.png"  align="center" />
  <h1 align="center">Scientific Calculation Bot</h2>
</p>
<p align="center">
    <img src="https://img.shields.io/github/v/release/fentaniao/ScientificCalculationBot?&color=blue&logo=hack-the-box" />
    <img alt="ChatBot" src="https://img.shields.io/badge/-ChatBot-3572A5?style=flat&logo=ChatBot&logoColor=white" />
    <img alt="Python" src="https://img.shields.io/badge/-Python-3572A5?style=flat&logo=python&logoColor=white" />
    <img alt="CQ-HTTP" src="https://img.shields.io/badge/-CQ--HTTP-3572A5?style=flat&logo=tencentqq&logoColor=white" />
</p>
基于Python 科学计算和绘图库和CQ-HTTP框架开发，提供基于QQ客户端的端到端服务，集科学计算、绘图、排版、聊天互动、群聊管理等功能为一体的智能QQ机器人。

由于CQ-HTTP于2020年秋已经停止服务，故本项目停止维护。

## 特色

### 端到端服务

用户只需要从QQ发送消息，消息即可被机器人捕获并进行处理。机器人将通过文字消息或是LaTeX引擎渲染出图片返回结果。

### 基于Python库和云的强大功能

本项目调用了多个Python库、Wolfram、阿里云、腾讯云等来实现机器人的各种功能。

### 科学计算与绘图

具有娱乐性功能的QQ机器人非常常见，但是具备科学计算和绘图的QQ机器人却非常少见。本机器人重点打造了科学计算和绘图的功能，基于SymPy库实现的科学计算功能，可以用简单的语法实现SymPy库中的各种功能，而基于matplotlib库实现的绘图功能，则通过了多种函数来实现各种简单或复杂的绘图任务。

## 主要功能

### 科学计算

<p>
    <img alt="numpy" src="https://img.shields.io/badge/package-numpy-3572A5?style=flat&logoColor=white" />
    <img alt="SymPy" src="https://img.shields.io/badge/package-SymPy-3572A5?style=flat&logoColor=white" />
</p>
科学计算功能由Python的numpy库和SymPy库提供，可以计算Python格式的表达式，并通过QQ文字消息或图片消息回复结果。现有功能包括：

- 符号表示
- 恒等变换
- 化简
- 解方程
- 极限
- 微积分
- 微分方程
- ......

[点击文档](https://github.com/Fentaniao/ScientificCalculationBot/blob/main/doc/ScientificCalculation.md)查看详细内容。

### 绘图

<p>
	<img alt="matplotlib" src="https://img.shields.io/badge/package-matplotlib-3572A5?style=flat&logoColor=white" />
</p>
绘图功能由Python的matplotlib库提供，提供多个接口实现不同种类函数的绘图绘制，并通过QQ图片消息的形式回复绘制好的图片。现有功能包括：

- 一元显函数
- 二元隐函数
- 参数方程

[点击文档](https://github.com/Fentaniao/ScientificCalculationBot/blob/main/doc/Plot.md)查看详细内容。

### 聊天互动和群聊管理

<p>
    <img alt="coolQ" src="https://img.shields.io/badge/-coolQ-3572A5?style=flat&logo=tencentqq&logoColor=white" />
</p>

通过对coolQ提供的接口进行二次开发，实现聊天互动和群聊管理等基础功能。现有功能包括：

- 基础互动
- 群聊管理
- 处理请求
- 获取信息
- 自检

[点击文档](https://github.com/Fentaniao/ScientificCalculationBot/blob/main/doc/Interaction.md)查看详细内容。

### 实用功能

<p>
    <img alt="Wolfram" src="https://img.shields.io/badge/-Wolfram-3572A5?style=flat&logo=Wolfram&logoColor=white" />
    <img alt="Wolfram Language" src="https://img.shields.io/badge/-Wolfram_Language-3572A5?style=flat&logo=WolframLanguage&logoColor=white" />
    <img alt="Alibaba Cloud" src="https://img.shields.io/badge/-Alibaba_Cloud-3572A5?style=flat&logo=AlibabaCloud&logoColor=white" />
    <img alt="Tecent Cloud" src="https://img.shields.io/badge/-Tecent_Cloud-3572A5?style=flat&logo=tencentqq&logoColor=white" />
</p>
围绕云和Python开发的一系列实用程序。现有功能包括：

- 科学百科
- 发送语音
- 若干实验性功能(Beta)

[点击文档](https://github.com/Fentaniao/ScientificCalculationBot/blob/main/doc/Utilities.md)查看详细内容。

## Contact

Author: Fentaniao

Email: [Fentaniao@gmail.com](mailto:Fentaniao@gmail.com)

## License

[GPL-3.0 License](https://github.com/Fentaniao/ScientificCalculationBot/blob/main/LICENSE) © Fentaniao
