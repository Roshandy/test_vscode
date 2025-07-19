from translate_DNA import translate_DNA

def flag_limit_area(animal, limit_area, DNA_bit, Int_bit, DNA_num):  # 判断种群是否符合值域，否则一票否决
    x, y = translate_DNA(animal, DNA_bit, Int_bit, DNA_num)
    if x <= limit_area[1] and x >= limit_area[0] and y <= limit_area[1] and y >= limit_area[0]:
        return True
    else:
        return False