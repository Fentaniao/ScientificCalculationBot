<p align="center">
 <img width="100px" src="README.assets/logo.png"  align="center" />
  <h1 align="center">Scientific Calculation Bot</h2>
</p>
<p align="center">
    <img src="https://img.shields.io/github/v/release/fentaniao/ScientificCalculationBot?&color=blue&logo=hack-the-box"/>
    <img alt="ChatBot" src="https://img.shields.io/badge/-ChatBot-3572A5?style=flat&logo=ChatBot&logoColor=white" />
    <img alt="Python" src="https://img.shields.io/badge/-Python-3572A5?style=flat&logo=python&logoColor=white" />
    <img alt="CQ-HTTP" src="https://img.shields.io/badge/-CQ--HTTP-3572A5?style=flat&logo=tencentqq&logoColor=white" />
</p>
<p align="center">
	<a href="https://github.com/Fentaniao/ScientificCalculationBot/blob/main/README.md">English Readme</a> • 
	<a href="https://github.com/Fentaniao/ScientificCalculationBot/blob/main/README_zh.md">中文自述文件</a>
</p>

An intelligent QQ bot based on Python scientific calculation and drawing library and CQ-HTTP framework, providing end-to-end services based on QQ client, and integrating scientific calculation, drawing, layout, chat interaction, group manage and other functions.

:warning: **This project stops maintenance because CQ-HTTP framework has been discontinued in the fall of 2020.**

## Features

### End-to-end service

Users only need to send messages from QQ, and then the messages will be captured and processed by the bot. The bot will return the results either through text messages or images rendered by the $\LaTeX$ engine.

### Based on powerful Python library and cloud

This project calls several Python libraries, Wolfram, AliCloud, Tencent Cloud, etc. to implement various functions of the bot.

### Scientific calculation and drawing

QQ bots with entertaining features are very common, but QQ bots with scientific calculation and drawing are very rare. This bot focuses on scientific calculation and plotting. The scientific calculation function based on the SymPy library can use a simple syntax to implement various functions in the SymPy library, while the plotting function based on the matplotlib library uses a variety of functions to implement various simple or complex plotting tasks.

## Main functions

### Scientific calculation

<p>
    <img alt="numpy" src="https://img.shields.io/badge/package-numpy-3572A5?style=flat&logoColor=white" />
    <img alt="SymPy" src="https://img.shields.io/badge/package-SymPy-3572A5?style=flat&logoColor=white" />
</p>

Scientific calculation functionality is provided by Python's numpy library and SymPy library, which can compute expressions in Python format and reply to the results via QQ text messages or image messages. Available features include

- symbolic representation
- constant transformations
- simplify
- Solving equations
- Limits
- Calculus
- Differential equations
- ......

[Click on the document](https://github.com/Fentaniao/ScientificCalculationBot/blob/main/doc/ScientificCalculation.md) for details.

### Plot

<p>
	<img alt="matplotlib" src="https://img.shields.io/badge/package-matplotlib-3572A5?style=flat&logoColor=white" />
</p>

The plotting functionality is provided by Python's matplotlib library, which provides several interfaces to implement different kinds of functions for plotting and replying to the plotted image via a QQ image message. Available functions include

- one-dimensional explicit functions
- binary implicit functions
- Parameter equations

[Click on the document](https://github.com/Fentaniao/ScientificCalculationBot/blob/main/doc/Plot.md) for details

### Chat interaction and group management

<p>
    <img alt="coolQ" src="https://img.shields.io/badge/-coolQ-3572A5?style=flat&logo=tencentqq&logoColor=white" />
</p>

The basic features such as chat interaction and group chat management are implemented by secondary development of the interface provided by coolQ. Existing features include

- Basic interaction
- Group chat management
- Handling requests
- Get information
- Self-check

[Click on the document](https://github.com/Fentaniao/ScientificCalculationBot/blob/main/doc/Interaction.md) for details.

### Useful functions

<p>
    <img alt="Wolfram" src="https://img.shields.io/badge/-Wolfram-3572A5?style=flat&logo=Wolfram&logoColor=white" />
    <img alt="Wolfram Language" src="https://img.shields.io/badge/-Wolfram_Language-3572A5?style=flat&logo=WolframLanguage&logoColor=white" />
    <img alt="Alibaba Cloud" src="https://img.shields.io/badge/-Alibaba_Cloud-3572A5?style=flat&logo=AlibabaCloud&logoColor=white" />
    <img alt="Tecent Cloud" src="https://img.shields.io/badge/-Tecent_Cloud-3572A5?style=flat&logo=tencentqq&logoColor=white" />
</p>

A series of utilities developed around the cloud and Python. Available features include

- Science Encyclopedia
- Voice Message
- Several experimental features (Beta)

[Click on the document](https://github.com/Fentaniao/ScientificCalculationBot/blob/main/doc/Utilities.md) for details.

## Contact

Author: Fentaniao

Email: [Fentaniao@gmail.com](mailto:Fentaniao@gmail.com)

## License

[GPL-3.0 License](https://github.com/Fentaniao/ScientificCalculationBot/blob/main/LICENSE) © Fentaniao
