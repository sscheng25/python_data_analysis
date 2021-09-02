# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:49:27 2020

@author: CSS
"""

from matplotlib import pyplot as plt
import random
#import matplotlib
from matplotlib import font_manager

#font = {'family':'Microsoft Yahei',
#        'weight':'bold'}
##        'size':'x-large'}
#matplotlib.rc("font",**font)
##matplotlib.rc("font",family='MicroSoft YaHei')

#另外一种设置字体的方法（通用）
my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")

x = range(0,120)
a = [random.randint(20,35) for i in range(120)]

fig = plt.figure(figsize=(20,8),dpi=60)

plt.plot(x,a)

#调整x、y轴刻度
_x = list(x)
_xtick_labels = ["10点{}分".format(i) for i in range(59)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(_x[::5],_xtick_labels[::5],rotation=90,fontproperties=my_font)
plt.yticks(range(min(a),max(a)+2))

#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度 单位(℃)")
plt.title("温度变化情况")

plt.show()
