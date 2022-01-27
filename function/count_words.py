# 这是一个统计单词出现次数的程序

# 输入端
# 输入待统计的字符串
# article = '''
# When I began coding back in 2013, I wasn’t obsessed with data structures and it turned out fine, but just fine, not exceptional!.
# I had to learn data structures and algorithms as these are the core concepts in computer science that helps one understand what is really going on behind your code.
# Learning this has significantly improved my coding skills, plus you also learn how to solve and optimize coding problems better.
#
# These days, programming beginners are more focused on the shining technologies.
# “Social media programmers” and bloggers flaunt various technologies and tutorials of how they’re used.
# This is not a bad thing but it’s becoming more and more distracting and make beginners jump right into learning these frameworks.
#
# I am guilty of this. When I began coding, I was straight to jump into the technologies and latest frameworks.
# I learnt a lot this way and also learnt how to solve different problems, but it’s not enough.
# '''


article =input('Paste the article here: ')


# 处理
def pretreatment(article):
    # 预处理
    # part 1: 格式化
    # 全文转为小写（但指定的的单词依然保持原样），删去无关字符
    article = article.lower()
    table = article.maketrans('', '', '!:(),.;“”’""[]#\n\r\r\n')
    article = article.translate(table)
    article = article.replace('i ', 'I ').replace('ive ', 'I have').replace('ihave', 'I have')
    # part 2: 拆分
    # 拆分得到单词列表
    words_list = article.split(' ')
    return words_list


words_list = pretreatment(article)

# 统计单词在单词列表中的出现次数，生成以单词为键，单词出现次数为值的字典,并对字典进行处理
word_n_dict = {}
for word in words_list:
    if word in word_n_dict:
        word_n_dict[word] = word_n_dict[word] + 1
    else:
        word_n_dict[word] = 1

try:
    word_n_dict.pop('')
except:
    pass

# 由上一步的字典，生成以单词出现次数为键，对应单词放进列表中为值的新字典
n_words_dict = {}
for word in word_n_dict:
    if word_n_dict[word] in n_words_dict:
        n_words_dict[word_n_dict[word]].append(word)
    else:
        n_words_dict[word_n_dict[word]] = [word]

# 分别按照出现次数和单词在字母表里的顺序进行排序
words_by_n_list = [None] * (max(n_words_dict) + 1)
for n in n_words_dict:
    n_words_dict[n].sort()
    words_by_n_list[n] = n_words_dict[n]


# 输出端
# 以语句形式在控制台输出
def state_result(words_by_n_list):
    times = len(words_by_n_list)
    for i in words_by_n_list:
        if i is not None:
            remind = times % 10
            if remind == 1:
                suffix = 'st'
            elif remind == 2:
                suffix = 'nd'
            elif remind == 3:
                suffix = 'rd'
            else:
                suffix = 'th'
            print('Words [' + ', '.join(i) + ' ] appear ' + str(times) + suffix + ' time(s).')
        times -= 1


# 以表格形式在控制台输出
def table_result(words_by_n_list):
    from prettytable import PrettyTable  # 导入库

    table = PrettyTable(['出现次数', '对应单词'])  # 设置列名

    times = len(words_by_n_list)  # 用for循环逐个添加行
    for i in words_by_n_list:
        if i != None:
            table.add_row([times, ', '.join(i)])
        times -= 1

    table.align = 'l'  # 左对齐
    print(table)  # 输出表格


state_result(words_by_n_list)
table_result(words_by_n_list)

# 以图片的形式输出结果为表格
# import matplotlib.pyplot as plt
# col_labels = ['col1', 'col2', 'col3']
# row_labels = ['row1', 'row2', 'row3']
# table_vals = [[11, 12, 13], [21, 22, 23], [28, 29, 30]]
# row_colors = ['red', 'gold', 'green']
# my_table = plt.table(cellText=table_vals, colWidths=[0.1] * 3, rowLabels=row_labels, colLabels=col_labels,
#                      rowColours=row_colors, colColours=row_colors, loc='center')
# def plt_result():
# col_labels = ['num', 'words']
# table_vals = []
# for outkey in outdict:
#     table_vals.append([outkey, outdict[outkey]])
# row_colors = ['red']
# my_table = plt.table(cellText=table_vals, colWidths=[0.5] * 2, colLabels=col_labels,
#                      colColours=row_colors * 2, loc='center')
# plt.show()