import random

def create_answer(number_set, n, m):  
    '''
    从初始数组随机选择m个数作为1组答案,共选择n组

    参数：
    number_set: 初始数组
    n: 不同答案的组数
    m: 每组答案元素的数量

    返回：
    n x m 的二维列表
    '''
    result = []
    for i in range(n):
        result.append(random.sample(number_set, m))
    return result

