def error_level(new_answer, number_set): 
    '''
    优胜劣汰：计算错误率,错误率越小遗传的概率越大

    参数：
    new_answer: 新的100组答案
    number_set: 初始数组

    返回：
    list: 100组初始答案的适应度
    '''
    error = []
    right_answer = sum(number_set) / 10
    for item in new_answer:
        value = abs(right_answer - sum(item))
        if value == 0:
            error.append(+1.0E10)
        else:
            error.append(1 / value)
    return error
