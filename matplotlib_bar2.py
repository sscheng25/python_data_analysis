# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 22:53:25 2020

@author: CSS
"""

from matplotlib import pyplot as plt
from matplotlib import font_manager

figure = plt.figure(figsize=(20,8),dpi=100)
my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

_x = list(range(len(a)))
_bar_width = 0.2

#_xticks = 
plt.xticks([i+_bar_width for i in _x],a,fontproperties=my_font)
plt.xlabel("电影名称",fontproperties=my_font)
plt.ylabel("票房：万元",fontproperties=my_font)

plt.bar(_x,b_14,width=_bar_width,label="9月14日")
plt.bar([i+_bar_width for i in _x],b_15,width=_bar_width,label="9月15日")
plt.bar([i+_bar_width*2 for i in _x],b_16,width=_bar_width,label="9月16日")

plt.legend(prop=my_font,loc=2)


