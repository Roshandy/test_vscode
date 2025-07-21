import numpy as np
from get_fitness import get_fitness
from translate_DNA import translate_DNA
from objective_function import f

def get_result(animals, limit_area, DNA_bit, Int_bit, DNA_num):  # 获取结果
    fitness = get_fitness(animals, limit_area, DNA_bit, Int_bit, DNA_num)
    max_fitness_index = np.argmax(fitness)
    print("max_fitness:", fitness[max_fitness_index])
    x, y = translate_DNA(animals[max_fitness_index], DNA_bit, Int_bit, DNA_num)
    print("最优的基因型：", animals[max_fitness_index])
    print("(x, y):", (x, y), f(x, y))
    return
