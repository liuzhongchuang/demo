# @Time    : 2018/11/29 0029 19:03
# @Author  : lzc
# @File    : 图形绘制.py
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

x = range(30)#边框长度
plt.plot(x)

#因为图形标题为中文乱码，采用系统自带字体库解析
jianti_cuti = FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
# 给图形设定标题
plt.title("金庸小说", FontProperties=jianti_cuti, fontsize = 18)

plt.show()


#将金庸小说人物名称读取出来格式化
with open(r'F:\xiaoshuo\name.txt', 'r', encoding='utf-8') as fl:
    data = [lines.strip() for lines in fl.readlines()]

#从文本中通过步长取出人物名称
names = data[1::2]
#从文本中取出书名
node = data[0::2]
print(names)
print(node)

# 将书名和人物名对应成字典格式
node_name =dict(zip(node, names))

print(node_name['天龙八部'])

with open(r'F:\xiaoshuo\天龙八部.txt', 'r', encoding='utf-8') as fl:
    data = fl.read()

#名字出现次数的集合
name_count = []
# 将人物在小说中出现的次数统计出来，然后放到count
for name in node_name['天龙八部'].split():
    name_count.append([name,data.count(name)])

#对人物次数进行排序
name_count.sort(key=lambda x:x[1], reverse=True)
print(name_count)

#绘制横坐标,实际上就是name_count中的第二个元素
name = [x[0] for x in name_count]
counts = [x[1] for x in name_count]

print(name)
print(counts)

# 绘制基本属性

plt.barh(range(10), counts, color='red', align='center')
# plt.py.barh(range(10), counts, color='red', align='center')