# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

from matplotlib import pyplot as plt
x = range(2,26,2)
y = [15,13,14,17,28,25,26,26,24,22,18,15]

#设置图片大小
fig = plt.figure(figsize=(20,8),dpi=40)

#绘图
plt.plot(x,y)

#设置x、y轴刻度
_xtick_labels = [i/2 for i in range (4,49)]
plt.xticks(_xtick_labels[::3])
plt.yticks(range(min(y),max(y)+2))

#保存
#plt.savefig("./sig_size.png")
#plt.show()
