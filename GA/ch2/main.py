# 问题描述：将一复杂函数作为目标函数，求解其最大值，模拟生物的生存环境

import numpy as np
import math
from flag_limit_area import flag_limit_area
from get_fitness import get_fitness
from select_animal import select_animal
from crossover_variation import crossover_and_variation

# 初始化参数
DNA_bit = 13 # 一个DNA的二进制位数,(第一维表示符号位)
Int_bit = 2  # DNA_bit-1（符号位bit）之后整数占的bit位
DNA_num = 2  # DNA的个数
animal_num = 200 # 开始种群的数量 
cross_rate = 0.8 # 生殖交叉概率
variation_rate = 0.005  # 变异的概率
generator_n = 50 # 种群演变的次数
limit_area = [-3, 3] # 值域

# 初始化种群，需要判断开始的种群是否符合值域
# 每个animal由两个DNA组成，每个DNA为DNA_bit位
# 2: 输出整数的上限
# size: 输出数组的形状
animals = np.random.randint(2, size=(animal_num, DNA_bit * DNA_num))

num = animal_num
while(num):
    pos = num - 1
    if flag_limit_area(animals[pos], limit_area, DNA_bit, Int_bit, DNA_num):
        num -= 1
    else:
        animals[pos] = np.random.randint(2, size=(1, DNA_bit * DNA_num))

# 模拟进化选择generator_n轮    
for i in range(generator_n):
    fitness_score = get_fitness(animals)
    selected_animals = select_animal(animals, fitness_score, animal_num)
    animals = crossover_and_variation(selected_animals, animals, cross_rate, variation_rate, animal_num, DNA_bit, DNA_num)

get_result(animals)
