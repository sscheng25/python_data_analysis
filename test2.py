# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 01:05:42 2020

@author: CSS
"""

from matplotlib import pyplot as plt

figure = plt.figure(figsize=(20,8),dpi=40)

a = [1,2,3,4,5,5,6,6,6,7,9,10]


bin_width=3
_xticks = list(range(min(a),max(a)+bin_width)[::3])
print (_xticks)

#plt.xticks = (range(min(a),max(a)+bin_width,bin_width))
#print ((range(min(a),max(a)+bin_width,bin_width)))
plt.xticks = (_xticks,_xticks)
#plt.xticks = ([1,2,3,4,5,6,7,8,9,10])

plt.grid()
plt.hist(a,bin_width)

plt.show()
