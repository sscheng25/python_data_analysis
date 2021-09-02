# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 16:59:44 2020

@author: CSS
"""

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")

a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_a = range(1,32)
x_b = range(51,82)

plt.figure(figsize=(20,8),dpi=100)

_x = list(x_a)+list(x_b)
_xtick_labels = ["3月{}日".format(i) for i in x_a]
_xtick_labels += ["10月{}日".format(i) for i in x_b]
plt.xticks(_x,_xtick_labels,fontproperties=my_font,rotation=90)
plt.yticks(range(5,30))

plt.xlabel("日期",fontproperties=my_font)
plt.ylabel("温度：℃",fontproperties=my_font)
plt.title("温度散点图",fontproperties=my_font)

plt.scatter(x_a,a,label="三月")
plt.scatter(x_b,b,label="十月")

plt.grid(alpha=0.3)
plt.legend(prop=my_font,loc="upper left")

plt.savefig("./scatterplot_temperature.png")