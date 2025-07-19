import numpy as np

def f(x, y):
    '''
    定义环境: 定义目标函数

    参数:
    int x 范围[-3,3]
    int y 范围[-3,3]
    '''
    return 3*(1-x)**2*np.exp(-(x**2)-(y+1)**2)- 10*(x/5 - x**3 - y**5)*np.exp(-x**2-y**2)- 1/3**np.exp(-(x+1)**2 - y**2)
