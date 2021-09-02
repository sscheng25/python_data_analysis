
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = plt.figure(figsize = (20,8),dpi = 80)

_interval = [0,5,10,15,20,25,30,35,40,45,60,90]
_width = [5,5,5,5,5,5,5,5,5,15,30,60]
_quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

_x = [i-0.5 for i in range(12)]
#_x_labels = ("")
plt.xticks(_x,_interval)

plt.bar(range(12),_quantity,width=1)
plt.grid(alpha = 0.3)

plt.show()



