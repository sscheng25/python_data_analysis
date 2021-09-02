import numpy as np
import random

#数组基础与数组的形状
t1 = np.array([1,2,3,4])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)

t3 = np.arange(10)
print(t3)
print(t3.dtype)

t4 = np.array(range(1,4),dtype="i1")
print(t4)
print(t4.dtype)

t5 = np.array([1,1,0,1,0,0],dtype=bool)
print(t5)

t6 = t5.astype("int8")
print(t6)

#numpy中的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

#取小数（四舍五入）
t8 = np.round(t7,2)
print(t8)

#shape和reshape
t9 = np.array(range(12))
print(t9)
t9.shape
t10 = t9.reshape(3,4)
print(t10)
print(t9.shape)
t10.reshape(1,12)   #不是一维数组
t10.flatten()   #是一维数组

#数组的计算
#数组可以直接加减乘，即为每个元素加减乘
t11 = t10+1
print(t11)

#同维数组也可以直接加乘，即为相对应位置的数值+/*
#不同维数组


