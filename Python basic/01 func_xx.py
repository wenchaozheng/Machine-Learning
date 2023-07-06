# -*- coding:utf-8 -*-
# @Author: WEN
# @Time: 2023/7/6 21:20
# @File: func_xx.py

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
y = x**x

plt.plot(x, y, 'r-', linewidth = '3')
plt.show()
