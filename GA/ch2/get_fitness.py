import numpy as np
from objective_function import f
from translate_DNA import translate_DNA
from flag_limit_area import flag_limit_area

def get_fitness(animals, limit_area, DNA_bit, Int_bit, DNA_num):
    '''
    计算种群各个部分的适应度

    参数:
    animal: 一个生物(NDA的组合)
    limit_area: x,y的定义域
    DNA_bit: 一个DNA的二进制位数,(第一维表示符号位)
    Int_bit: DNA_bit-1(符号位bit)之后整数占的bit位
    DNA_num: DNA的个数

    输出:
    种群各个部分的适应度
    '''
    fitness_score = np.zeros(len(animals))
    fit_flag = np.zeros(len(animals))
    for i in range(len(animals)):
        x, y = translate_DNA(animals[i], DNA_bit, Int_bit, DNA_num)
        fitness_score[i] = f(x, y)
        if flag_limit_area(animals[i], limit_area, DNA_bit, Int_bit, DNA_num):
            fit_flag[i] = 1
        else:
            fit_flag[i] = 0
    fitness_score = (fitness_score - np.min(fitness_score)) + 1e-5
    fitness_score = fitness_score * fit_flag # 如果不符合定义域就不取了
    fitness_p = fitness_score / (fitness_score.sum())  # 计算被选择的概率
    return fitness_p 
