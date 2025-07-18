# 问题描述：在一个长度为n的数组nums中选择10个元素，使得10个元素的和与原数组的所有元素之和的1/10无限接近
# 问题举例：如n=50, sum(nums)=1000, 选择元素列表answer要满足|sum(answer)-100|<e,e尽可能小

import random
from create_answer import create_answer
from error_level import error_level
from choice_selected import choice_selected
from variation import variation

# 初始化种群：随机选择100组答案
number_set = random.sample(range(0, 1000), 50)
middle_answer = create_answer(number_set, 100, 10) 

# 定义最初解和最优解 
first_answer = middle_answer[0]
greater_answer = []

for i in range(1000):  
    # 交叉繁殖变异
    middle_answer = choice_selected(middle_answer, number_set)
    middle_answer = variation(middle_answer, number_set, 0.1)

    # 计算适应度
    error = error_level(middle_answer, number_set) 
    index = error.index(max(error))

    # 记录每一轮遗传进化的最优解
    greater_answer.append([middle_answer[index], error[index]])

# 输出打印求解结果
''' 
函数sort(排序):
key=lambda x: x[1]表示按第二个元素排序；
reverse参数控制排序的「升序」和「降序」,True表示降序,False表示升序
'''
greater_answer.sort(key=lambda x: x[1], reverse=True)
print("最初解的和为", sum(first_answer))
print("正确答案为", sum(number_set) / 10)
print("给出最优解为", greater_answer[0][0])
print("该和为", sum(greater_answer[0][0]))
print("选择系数(适应度)为", greater_answer[0][1])
print("最优解之和与正确答案的差距为", abs(sum(number_set) / 10 - sum(greater_answer[0][0])))


