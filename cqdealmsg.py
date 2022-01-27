# 导入调用的文件
from cqoutput import *
from function import cqsym

# 导入库
import time
import re

# 解josn

# 导入词库和拆分库
import pkg_resources
from symspellpy.symspellpy import SymSpell

# 导入科学计算和绘图库
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')
matplotlib.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# from sympy import *
# from sympy.plotting import plot

# 保存位置
plt_path = ''

# 向以下群提供服务
group_list = []

# 话语跟踪
id_saying = {}

# 语言库：{(关键词)：[应答]}
# 单个元素构成的元组需要在元素尾加上一个 ,表示这是个元组，否则，Python会以为你只是写了个整数，然后给整数加了个数学意义的小括号运算符
corpus = {
    (r'(.*)怎么(.*)使用.*', r'(.*)菜单(.*)', r'(.*)帮助(.*)',): [
        '直接说“计算帮助”，可以获取计算功能的说明', ],
    (r'(.*)计算帮助(.*)',): [
        '计算帮助列表：\n'
        + '\n'.join(['输出结果', '符号表示', '恒等变换', '化简', '解方程', '极限', '微积分', '微分方程'])
        + '\n直接说“模块：需要的条目”，可以显示对应模块的说明\n如：模块：微积分'],
    (r'(.*)绘图帮助(.*)',): [
        '[CQ:image,file=' + str('绘图模式.png') + "]"],

    ('我最爱学妹了',): [
        '这样才对嘛'],
    (r'(.*)龙王(.*)咒语.*', r'(.*)龙王(.*)喷(.*)水.*',): [
        '呼风唤雨', '84消毒'],
    (r'(.*)自我(.*)介绍.*',): [
        '我是学妹，是一个集科学计算、绘图、聊天互动、群管为一体的智能机器人', ],
}

# 从语言库生成关键词字典
word_trans = {}
for corpus_key in corpus:
    for word in corpus_key:
        word_trans[word] = corpus_key

# wolfram alpha会话式回答
conversational_user_id = {}


# 格式化message，一方面增强读取message的鲁棒性，另一方面简化输入
def msg_format(message):
    intab = """，。‘’“”（）【】；"""
    outtab = """,.''""()[];"""
    tab = message.maketrans(intab, outtab)  # 这里的英文冒号和中文冒号居然相反？？？
    message = message.translate(tab)

    # message = message.replace('^', '**')

    message = message.strip()

    link_dict = {'group_': 'group_manage(group_id).',
                 'get_group_': 'get_group(group_id).',
                 }
    for string in link_dict:
        index = 0
        while 0 <= index <= len(message):
            index = message.find(string, index)
            if index >= 0:
                message = message[:index] + link_dict[string] + message[index:]
                index = index + len(link_dict[string]) + 1

    return message


def split_word(message):
    sym_spell = SymSpell(max_dictionary_edit_distance=0, prefix_length=7)
    dictionary_path = pkg_resources.resource_filename(
        "symspellpy", "frequency_dictionary_en_82_765.txt")

    sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

    # a sentence without any spaces
    input_term = message
    result = sym_spell.word_segmentation(input_term)
    return result.corrected_string


def wolfram_format(message):
    return message.replace("+", " plus ").replace("=", " = ")


# def delte_n(message):
#     tab = message.maketrans('', '', '\n')
#     message = message.translate(tab)
#     return message

def deal(user_id, group_id, discuss_id, nickname, message):
    # 显示结果：通过发送私聊/群聊/讨论组消息（弱功能）
    def show(message):
        if group_id is not None:
            message_type = 'group'
            id = group_id
        elif discuss_id is not None:
            message_type = 'discuss'
            id = discuss_id
        else:
            message_type = 'user'
            id = user_id

        data = {
            message_type + '_id': id,
            'message': str(message),
            'auto_escape': False
        }

        url_suffix = '/send_msg'
        requests.post('http://127.0.0.1:5700' + url_suffix, data=data)

    def feature(message):
        message = str(message)
        ax = plt.subplot(111)

        message = eval('latex(' + message + ')')

        spnum_list = [0]
        line_num = 0

        index_plus_old = 0
        while True:
            index_plus_new = message.find('+', index_plus_old + 1)
            if index_plus_new == -1:
                break
            num_l_bracket = message.count('(', index_plus_old, index_plus_new)
            index_l_bracket = message.find('(', index_plus_old, index_plus_new)
            num_r_bracket = message.count(')', index_plus_old, index_plus_new)
            index_r_bracket = message.find(')', index_plus_old, index_plus_new)
            if num_l_bracket <= num_r_bracket and index_l_bracket <= index_r_bracket:
                spnum_list.append(index_plus_new)
            index_plus_old = index_plus_new

        index_minus_old = 0
        while True:
            index_minus_new = message.find('-', index_minus_old + 1)
            if index_minus_new == -1:
                break
            num_l_bracket = message.count('(', index_minus_old, index_minus_new)
            index_l_bracket = message.find('(', index_minus_old, index_minus_new)
            num_r_bracket = message.count(')', index_minus_old, index_minus_new)
            index_r_bracket = message.find(')', index_minus_old, index_minus_new)
            if num_l_bracket <= num_r_bracket and index_l_bracket <= index_r_bracket:
                spnum_list.append(index_minus_new)
            index_minus_old = index_minus_new

        spnum_list.sort()
        spnum_list.append(len(message))

        for num in range(len(spnum_list) - 1):
            sp1 = spnum_list[num]
            sp2 = spnum_list[num + 1]
            ax.text(-0.1, 1.05 - 0.15 * line_num, r'$' + message[sp1:sp2] + '$', fontsize=17, color='black')
            line_num += 1

        plt.axis('off')
        plt.savefig(plt_path + '\\feature.jpg')
        show('[CQ:image,file=' + str('feature.jpg') + "]")
        plt.close()

    # 画一元显函数
    def draw(fun, x_arange):
        # draw_fun('sin(x) / x', '-10，10，0.1')
        plt.close()

        loc = locals()
        exec('t=arange(' + x_arange + ')')
        t = loc['t']

        y = []
        for x in t:
            y1 = eval(fun)
            y.append(y1)
        plt.plot(t, y)

        plt.title('函数y=' + fun)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()

        plt.savefig(plt_path + '\\test.jpg')
        send_msg('group', group_id, '[CQ:image,file=' + str('test.jpg') + "]")
        plt.close()

    # 画二元隐函数
    def draw_imp(equation, x_range, y_range):
        # draw_implicit('17 * x**2 -16*abs(x)*y + 17 * y**2-256','-6,6','-6,6')

        # 构造等高线函数
        def f(x, y):
            return eval(equation)

        # 定义点的数量
        n = 500

        # 作点
        x_str = 'linspace(' + x_range + ',500)'
        y_str = 'linspace(' + y_range + ',500)'
        x = eval(x_str)
        y = eval(y_str)

        # 构造网格
        X, Y = meshgrid(x, y)

        # 绘制图像
        plt.contour(X, Y, f(X, Y), 0)
        # 作其他图像

        plt.title('曲线方程：' + equation + '=0')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()

        plt.savefig(plt_path + '\\test.jpg')
        send_msg('group', group_id, '[CQ:image,file=' + str('test.jpg') + "]")
        plt.close()

    # 画单参数的参数方程：
    def draw_para(x_eq, y_eq, t_arrange):
        # draw_para('2*sin(t)','3*cos(t)','0, 2*pi, 0.1')

        plt.close()

        # 参数方程
        loc = locals()
        exec('t=arange(' + t_arrange + ')')
        t = loc['t']

        x = eval(x_eq)
        y = eval(y_eq)

        # 绘图
        fig = plt.figure()
        axes = fig.add_subplot(111)
        axes.plot(x, y)
        axes.axis('equal')

        plt.title('参数方程（t为参数）:\nx=' + x_eq + ', y=' + y_eq)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()

        plt.savefig(plt_path + '\\test.jpg')
        send_msg('group', group_id, '[CQ:image,file=' + str('test.jpg') + "]")
        plt.close()

    # 记录聊天
    if user_id not in id_saying:
        id_saying[user_id] = [message]
    else:
        if len(id_saying[user_id]) >= 20:
            id_saying[user_id] = []
        if len(id_saying) >= 30:
            id_saying.clear()
        id_saying[user_id].append(message)

    # 语言库
    for match in word_trans:
        if re.match(match, message, re.M | re.I):
            for part in corpus[word_trans[match]]:
                show(part)

    # wolframAPI

    appid = "?appid=EKWVPJ-5R9LJVH27X"

    # 简单结果
    def easy_res(query, appid=appid):
        base_url = "http://api.wolframalpha.com/v1/simple"
        query = "&i=" + query.replace(' ', '+')
        api_url = base_url + appid + query
        with open(plt_path + '\\easy_result.jpg', 'wb') as file:
            file.write(requests.post(api_url).content)
        send_msg('group', group_id, '[CQ:image,file=' + str('easy_result.jpg') + "]")

    # 完整结果
    # base_url = "http://api.wolframalpha.com/v2/query&format=image"
    # app_id = ""
    # query = "&input=population%20of%20france"
    # api_url = base_url + app_id + query
    # with open('picture.jpg', 'wb') as file:
    #     file.write(requests.post(api_url).content)

    # 简短回答
    def short_answers(query, appid=appid):
        base_url = "http://api.wolframalpha.com/v1/result"
        query = "&i=" + query.replace('+', 'plus').replace(' ', '+') + "%3f"
        api_url = base_url + appid + query
        show(requests.post(api_url).content)

    # 会话式
    def conversational(query, appid=appid):
        # 初次会话
        if user_id not in conversational_user_id:
            base_url = "http://api.wolframalpha.com/v1/conversation.jsp"
            query = "&i=" + query.replace('+', 'plus').replace(' ', '+') + "%3f"
            api_url = base_url + appid + query

        # 多次对话
        else:
            base_url = "http://" + conversational_user_id[user_id]["host"] + "/api/v1/conversation.jsp"
            query = "&i=" + query.replace('+', 'plus').replace(' ', '+') + "%3f"
            api_url = base_url + appid \
                      + "&conversationid=" + conversational_user_id[user_id]["conversationID"] \
                      + query

            if "s" in conversational_user_id[user_id]:
                api_url = api_url + "&s=" + conversational_user_id[user_id]["s"]

        answer = requests.post(api_url).json()  # 将json转换为字典

        conversational_user_id[user_id] = answer
        try:
            show(answer["result"])
        except:
            show(answer["error"])
            del conversational_user_id[user_id]

    # 召唤系统
    if message == '召唤学妹':
        show('快说“我最爱学妹了”')
        time.sleep(10)
        if '我最爱学妹了' not in id_saying[user_id]:
            show('都10s了还不说，分手吧')

    # wolfram查询
    elif message.startswith('query'):
        i = message[5]
        # 不输入i的值则默认i为1
        if i == ":":
            i = "1"

        # 截取分号之前的字符并进一步格式化字符串
        index = message.find(":")
        message = message[index + 1:]
        message = wolfram_format(split_word(message))

        # 根据i的值调用函数
        if i == "1":
            easy_res(message)
        elif i == "3":
            short_answers(message)
        elif i == "4":
            conversational(message)
        show("Finish query.")

    # elif message.startswith('模块：'):
    #     index1 = sym_readme.find('## ' + message[3:])
    #     index2 = index1 + 4
    #     while True:
    #         index2 = sym_readme.find('## ', index2 + 1)
    #         if sym_readme[index2 - 1] != '#':
    #             break
    #     display = '模块' \
    #               + sym_readme[index1:index2 - 1] \
    #               + '直接说“模板：###后的条目”，可以获取对应的模板,可以复制并修改.\n' \
    #                 '熟悉语法后，可自行编写代码进行，说“模板：自定义”，获取自定义模板。'
    #     show(display)
    #
    # elif message.startswith('模板：'):
    #     index1 = sym_readme.find('### ' + message[3:])
    #     new_index1 = sym_readme.find('```', index1)
    #
    #     index2 = index1 + 4
    #     while True:
    #         index2 = sym_readme.find('### ', index2 + 1)
    #         if sym_readme[index2 - 1] != '#':
    #             break
    #
    #     index3 = index1 + 4
    #     while True:
    #         index3 = sym_readme.find('## ', index3 + 1)
    #         if sym_readme[index3 - 1] != '#':
    #             break
    #     new_index2 = sym_readme.find('```', new_index1 + 4, min(index2, index3))
    #     display = 'sympy\n' + sym_readme[new_index1 + 4: new_index2 - 1] + '\nplay'
    #     show(display)

    else:
        if 0 <= message.find('play'):
            message = cqsym.image_format(message, group_id)
        try:
            time.sleep(0.2)
            exec(eval("\'\'\'" + message + "\'\'\'"))
        except:
            print('num: exit none command')
