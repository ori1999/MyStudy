import jieba
from collections import Counter
import json
import matplotlib.pyplot as plt
import matplotlib
import sys

#在引入jieba模块后加入这行代码，代码即可不报错
jieba.setLogLevel(jieba.logging.INFO)

#解决matplotlib显示中文乱码的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'

xianni = open('7115109098.txt', 'r', encoding='utf-8').read()
xianni_words = [x for x in jieba.lcut(
    xianni) if len(x) >= 2]  # 将全文分割，并将大于两个字的词语放入列表
c = Counter(xianni_words).most_common(160)  # 取最多的10组
print(json.dumps(c, ensure_ascii=False))
lista = [str(i) for i in range(0,100)]
lista += ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '用户', '组图',
          '主页', '2021', '2020',  '看看', '精选', '照片', '发布', '微博', '时间', '位置', '转发', '评论', '点赞数', '工具', '原图', '超话', '游戏']
print('================================',lista)
name_list = [x[0] for x in c[120:] if x[0] not in lista]  # X轴的值
num_list = [x[1] for x in c[120:] if x[0] not in lista]  # Y轴的值
b = plt.bar(range(len(num_list)), num_list, tick_label=name_list)  # 画图

plt.xlabel(u'词语')
plt.ylabel(u'次数')
plt.title(u'文本分词统计')
plt.show()  # 展示
