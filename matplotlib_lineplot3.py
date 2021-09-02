# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:15:08 2020

@author: CSS
"""

from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np 

my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")

x = np.arange(11,16,1)
a = [1,0,1,1,2]
#a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
b = [1,0,3,1,2]
#b = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

fig = plt.figure(figsize=(20,8),dpi=80)

_xtick_labels = ["{}岁".format(i) for i in x]

#xticks(np.arange(11, 30, step=1))
plt.xticks(np.arange(11, 16, step=1), ('11','12','13','14','15'))




#plt.xticks=(x = x, labels = _xtick_labels)
plt.yticks(range(0,9))

plt.xlabel("年龄")
plt.ylabel("数量：个")
plt.title("女朋友个数")

#绘制网格
plt.grid(alpha=0.4,linestyle='--')

plt.plot(x,a,label='A',color='red',linestyle=':')
plt.plot(x,b,label='B',color='cyan',alpha=0.5)

#添加图例
plt.legend(prop=my_font,loc=2)
plt.show()