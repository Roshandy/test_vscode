from translate_DNA import translate_DNA

def flag_limit_area(animal, limit_area, DNA_bit, Int_bit, DNA_num):  
    '''
    判断种群是否符合值域，否则一票否决

    参数:
    animal: 一个生物(NDA的组合)
    limit_area: x,y的定义域
    DNA_bit: 一个DNA的二进制位数,(第一维表示符号位)
    Int_bit: DNA_bit-1(符号位bit)之后整数占的bit位
    DNA_num: DNA的个数

    输出:
    x,y是否满足定义域的判断
    '''
    x, y = translate_DNA(animal, DNA_bit, Int_bit, DNA_num)
    if x <= limit_area[1] and x >= limit_area[0] and y <= limit_area[1] and y >= limit_area[0]:
        return True
    else:
        return False