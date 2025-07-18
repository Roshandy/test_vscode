import random
from error_level import error_level

def choice_selected(old_answer, number_set):  
    '''
    交配生殖:交叉互换模拟交配生殖的结果

    参数：
    old_answer: 旧的100组答案
    number_set: 初始数组

    返回：
    list: 新的100组答案
    '''
    result = []
    error = error_level(old_answer, number_set)
    error_one = [item / sum(error) for item in error]
    for i in range(1, len(error_one)):
        error_one[i] += error_one[i - 1]

    for i in range(len(old_answer) // 2):
        temp = []
        for j in range(2):
            # 生成0~1之间的随机浮点数
            rand = random.uniform(0, 1)
            for k in range(len(error_one)):
                if k == 0:
                    if rand < error_one[k]:
                        temp.append(old_answer[k])
                else:
                    if rand >= error_one[k-1] and rand < error_one[k]:
                        temp.append(old_answer[k])
        # 生成0~6之间的随机整数
        rand = random.randint(0, 6)
        # 优化部分（a,b）:设计随机的a和b使交叉繁殖后的数据更加随机化
        a = random.randint(0,len(temp)-1)
        b = random.randint(0,len(temp)-1)
        temp_a = temp[a][:rand] + temp[b][rand:rand+3] + temp[a][rand+3:]
        temp_b = temp[b][:rand] + temp[a][rand:rand+3] + temp[b][rand+3:]
        result.append(temp_a)
        result.append(temp_b)
    return result