# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 22:27:39 2020

@author: CSS
"""

from matplotlib import pyplot as plt
from matplotlib import font_manager

figure = plt.figure(figsize=(20,8),dpi=80)

a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]
b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23] 
my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")

_x = range(len(a))
plt.yticks(_x,a,fontproperties=my_font)
plt.xticks()

plt.title("2016年电影票房数据",fontproperties=my_font)
plt.ylabel("电影名",fontproperties=my_font)
plt.xlabel("票房：亿元",fontproperties=my_font)
#plt.grid(alpha=0.3)

plt.barh(a,b,color='orange',height=0.5)
plt.show()
