import re

word_cnt = {}


def parser(txt):
    # 使用正则表达式去除标点符号和换行符
    txt = re.sub(r'[^\w ]', ' ', txt)

    # 转为小写
    txt = txt.lower()

    # 生成所有单词的列表
    word_list = txt.split(' ')

    # 去除空白单词
    word_list = filter(None, word_list)

    # 生成单词和词频的字典
    global word_cnt
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1


with open('./data/in.txt') as file:
    for line in file:
        parser(line)


word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
print(word_cnt)
