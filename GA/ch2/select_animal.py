import numpy as np

def select_animal(animals, fitness, animal_num):  
    '''
    按照适应度选择留下的种群

    参数:
    animals: 一个生物群(所有NDA的组合)
    fitness: 适应度
    animal_num: 开始种群的数量

    输出:
    选择animal_num次各种群的序号
    '''
    idx = np.random.choice(np.arange(animal_num), size=animal_num, replace=True, p=(fitness)/(fitness.sum() + 1e-8))
    return animals[idx]
