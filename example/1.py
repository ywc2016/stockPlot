# -*- coding: utf-8 -*-
'''
饼图
'''

import matplotlib.pyplot as plt

# 为了在图表中能够显示中文和负号等，需要下面一段设置：
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

labels = 'frogs', 'hogs', '狗', 'logs'
sizes = 88, 20, 45, 10
colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral'
explode = 0, 0.1, 0, 0
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
plt.axis('equal')
plt.show()
