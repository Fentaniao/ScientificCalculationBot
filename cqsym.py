import time

from sympy import *
from sympy.abc import *
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')
matplotlib.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

from cqoutput import send_msg
import requests


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
        ax = plt.subplot(111)
        spnum_list = [0]
        line_num = 0

        message = str(message)

        message = eval('latex(' + message + ')')

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
        plt.savefig(fig_path+'\\feature.jpg')
        show('[CQ:image,file=' + str('feature.jpg') + "]")
        plt.close()

    if 0 <= message.find('play'):
        message = image_format(message, group_id)
    try:
        time.sleep(0.2)
        exec(eval("\'\'\'" + message + "\'\'\'"))
    except:
        print('sym: exit none command')


def image_format(message, group_id):
    play_list = message.split('play')
    for k in range(len(play_list) - 1):
        formula_image(play_list[k], group_id, k + 1)
        time.sleep(0.1)
    message = ''.join(play_list)
    return message


def formula_image(message, group_id, page=1):
    ax = plt.subplot(111)

    line_list = message.split('\n')  # 按\n将各行拆开 得到 各行字符串组成的行列表line_list
    for i in range(len(line_list)):
        line_list[i] = line_list[i].split('=')  # 按=将一行拆开 得到

    exclude_list = ['#', '\r', 'show']
    line_num = 0
    for i in range(len(line_list)):
        flag = False
        for start in exclude_list:
            flag = flag or line_list[i][0].startswith(start)
        flag = flag or line_list[i] == ['']

        if not flag:
            try:
                for j in range(len(line_list[i])):
                    line_list[i][j] = eval('latex(' + line_list[i][j] + ')')
                    line_list[i] = '='.join(line_list[i])
                    ax.text(-0.1, 1.05 - 0.15 * line_num, r'$' + line_list[i] + '$', fontsize=17, color='black')

            except:
                line_list[i] = '='.join(line_list[i])[:-1]
                ax.text(-0.1, 1.05 - 0.15 * line_num, line_list[i], fontsize=17, color='black')

        else:
            line_list[i] = '='.join(line_list[i])[:-1]
            ax.text(-0.1, 1.05 - 0.15 * line_num, line_list[i], fontsize=17, color='black')
        line_num += 1

    ax.text(0.95, 0, str(page), size=15,
            family="fantasy", color="g", style="oblique", weight="light",
            bbox=dict(facecolor="b", alpha=0.15))
    plt.axis('off')

    plt.savefig(fig_path+'\\formula.jpg')
    send_msg('group', group_id, '[CQ:image,file=' + str('formula.jpg') + "]")
    plt.close()
