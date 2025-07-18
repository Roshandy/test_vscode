import random

def variation(old_answer, number_set, pro):  
    '''
    0.1的变异概率

    参数：
    old_answer: 交叉繁殖过的100组答案
    number_set: 初始数组
    pro: 变异率

    返回：
    list: 新的100组答案
    '''
    for i in range(len(old_answer)):
        rand = random.uniform(0, 1)
        if rand < pro:
            rand_num = random.randint(0, 9)
            old_answer[i] = old_answer[i][:rand_num] + random.sample(number_set, 1) + old_answer[i][rand_num+1:]
    return old_answer
