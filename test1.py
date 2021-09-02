# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 01:05:42 2020

@author: CSS
"""

from matplotlib import pyplot as plt
import numpy as np

#figure = plt.figure(figsize=(20,8),dpi=60)

a = [1,2,3,4,5,5,6,6,6,7,9,10]


bin_width=3
#_xticks = list(range(min(a),max(a)+bin_width)[::3])
#print (_xticks)

#plt.plot(a,a)
plt.xticks([1, 4, 7, 10],['1','4','7','10'])



#_xticks2 = np.arange(0,11,1)
#print (_xticks2)
#plt.xticks = (_xticks2)

#fig, ax = plt.subplots()
#ax.set_xlim([0, 11])
#ax.set_ylim([0, 11])



#plt.xticks = (range(min(a),max(a)+bin_width,bin_width))
#print ((range(min(a),max(a)+bin_width,bin_width)))

#plt.xticks = ([1,2,3,4,5,6,7,8,9,10])

plt.grid()


plt.hist(x = a,bins = bin_width, range=None)

plt.show()
