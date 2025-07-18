import numpy as np
import math

# 初始化参数
DNA_bit = 13 # 一个DNA的二进制位数,(第一维表示符号位)
Int_bit = 2  # DNA_bit-1（符号位bit）之后整数占的bit位
DNA_num = 2  # DNA的个数
animal_num = 200 # 开始种群的数量 
cross_rate = 0.8 # 生殖交叉概率
variation_rate = 0.005  # 变异的概率
generator_n = 50 # 种群演变的次数
limit_area = [-3, 3] # 值域
