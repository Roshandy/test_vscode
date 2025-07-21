import numpy as np

def variation(children, variation_rate, DNA_bit, DNA_num):
    '''
    模拟变异
    '''
    if np.random.rand() < variation_rate: #以MUTATION_RATE的概率进行变异
        mutate_point = np.random.randint(0, DNA_bit * DNA_num)  # 随机产生一个实数，代表要变异基因的位置
        children[mutate_point] = children[mutate_point] ^ 1  #这一位取反
    return children
 

def crossover_and_variation(animals, cross_rate, variation_rate, animal_num, DNA_bit, DNA_num):  
    '''
    模拟生殖过程（包括交配和变异）

    参数:
    animals: 一个生物群(所有NDA的组合)
    cross_rate: 生殖交叉概率
    variation_rate: 变异的概率
    DNA_bit: 一个DNA的二进制位数,(第一维表示符号位)
    animal_num: 开始种群的数量
    DNA_num: DNA的个数

    输出:
    种群各个部分的适应度
    '''
    new_animals = []
    for father in animals:
        child = father		# 选择父亲
        if np.random.rand() < cross_rate:	#产生子代时不是必然发生交叉，而是以一定的概率发生交叉
            mother = animals[np.random.randint(animal_num)]	#再选择母亲
            cross_points = np.random.randint(low = 0, high = DNA_bit * DNA_num)	#随机产生交叉的点
            child[cross_points:] = mother[cross_points:] # 交叉互换，模拟生殖
        variation(child, variation_rate, DNA_bit, DNA_num)	#变异
        new_animals.append(child)
    return np.array(new_animals)
