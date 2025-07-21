import math

def translate_DNA(animal, DNA_bit, Int_bit, DNA_num):  
    '''
    解码种群的DNA(计算x,y)

    参数:
    animal: 一个生物(NDA的组合)
    DNA_bit: 一个DNA的二进制位数,(第一维表示符号位)
    Int_bit: DNA_bit-1(符号位bit)之后整数占的bit位
    DNA_num: DNA的个数

    输出:
    x,y
    '''
    def DNA2t10(DNA):
        '''
        二进制转换为十进制
        '''
        sum = 0
        sign = DNA[0]
        data = DNA[1:]

        # 符号位赋值
        if sign == 0:  
            flag = -1
        else:
            flag = 1       
        # 整数位赋值
        for i in range(0, Int_bit):
            if data[i] == 1:
                sum += math.pow(2, Int_bit - i - 1)
        # 小数位赋值
        for i in range(Int_bit, len(data)):
            if data[i] == 1:
                sum += math.pow(2, Int_bit - i - 1)
        return flag * sum
    
    DNA_result = []
    for i in range(0, DNA_bit * DNA_num, DNA_bit):
        DNA = animal[i:i+DNA_bit]
        translated_DNA = DNA2t10(DNA)
        DNA_result.append(translated_DNA)
    return DNA_result
