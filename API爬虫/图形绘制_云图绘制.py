# @Time    : 2018/11/30 0030 15:24
# @Author  : lzc
# @File    : 图形绘制_云图绘制.py

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties

# x = range(30)
# plt.plot(x)
#
# #因为图形标题为中文乱码，采用系统自带字体库解析
jianti_cuti = FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
mpl.rcParams['font.sans-serif']=['simhei']
# # 给图形设定标题
# plt.title("金庸小说", FontProperties=jianti_cuti, fontsize = 18)

# plt.show()


#将金庸小说人物名称读取出来格式化
with open(r'F:\xiaoshuo\name.txt', 'r', encoding='utf-8') as fl:
    data = [lines.strip() for lines in fl.readlines()]

#从文本中通过步长取出人物名称
names = data[1::2]
#从文本中取出书名
node = data[0::2]
# print(names)
# print(node)

# 将书名和人物名对应成字典格式
node_name =dict(zip(node, names))

print(node_name['倚天屠龙记'])

with open(r'F:\xiaoshuo\倚天屠龙记.txt', 'r', encoding='utf-8') as fl:
    data = fl.read()

#名字出现次数的集合
name_count = []
# 将人物在小说中出现的次数统计出来，然后放到count
for name in node_name['倚天屠龙记'].split():
    name_count.append([name,data.count(name)])

#对人物次数进行排序
name_count.sort(key=lambda x: x[1], reverse=True)
# print(name_count)

#绘制横坐标,实际上就是name_count中的第二个元素
name = [x[0] for x in name_count]
counts = [x[1] for x in name_count]

print(name)
print(counts)

for x in name_count[:10]:
    # 指定绘制图形的文本属性 ha指定字体在柱状的中间位置
    plt.text(x[0], x[1], '%.0f' % x[1], fontsize=14, ha='center')#绘制柱形图

# 设置横坐标和纵坐标
x = name[:10]
y = counts[:10]
#color里面的rgby表示红绿蓝黄颜色。图形按顺序反复渲染
plt.bar(x,y,color='rgby')
#设置y轴的上限
plt.ylim(0, 5000)
#设置y轴的注释信息
plt.ylabel('人物出现次数')
# 设置x轴的注释信息
plt.xlabel('人物名称')
# plt.show()


# import jieba
# import gensim
# for x in name_count:
#     # 将人名作为jieba分词的字典加入到jieba中
#     jieba.add_word(x[0])
#
# with open(r'F:\xiaoshuo\倚天屠龙记.txt', 'r', encoding='utf-8') as fl:
#     data = fl.readlines()
#
# #将书的每一行内容cut之后作为元素存放到word_list中
# word_list = []
# # 因为一本书的内容比较多，如果使用read读出来放在data里面做一次cut，需要花费很长时间，并且分割可能不准确
# for line in data:
#     words = list(jieba.cut(line))
#     word_list.append(words)
#
# model = gensim.models.Word2Vec(word_list, size=100)
#
#
# per = ['赵敏','周芷若','殷素素','杨不悔','灭绝师太']
#
# for x in per:
#     print('张无忌和%s的关联性为:' % x, model.wv.similarity('张无忌',x))



#云图
import codecs
import jieba.analyse as analyse
from wordcloud import *

#将文本内容使用codecs读取出来
bookContext = codecs.open(r'F:\xiaoshuo\倚天屠龙记.txt', 'r',encoding='utf-8').read()
# 使用jieba中的analyse对文本内容进行分析，以标签的形式，并且进行加粗
tags = analyse.extract_tags(bookContext, topK=100, withWeight=True)

dict_tags = dict((x) for x in tags)
print(dict_tags)

#使用wordcloud绘制云图标签
wc = WordCloud(font_path='C:\Windows\Fonts\simkai.ttf').generate_from_frequencies(dict_tags)
# facecolor图形底色，
plt.figure(facecolor='w',edgecolor='r')

#去掉横坐标和纵坐标
plt.axis('off')
plt.imshow(wc)
plt.show()



