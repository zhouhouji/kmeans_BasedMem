import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


# 自定义函数对数形式
def func(x, a, b):
    return a - b * np.log(x)

def readFiles(filename):
    rawData = pd.read_csv(filename)
    cycle = rawData.iloc[:, 0].values
    currentData = rawData.iloc[:, 1].values
    return cycle, currentData

def funcConducdence():
    # 打开的文件名
    filename = "LiSiO_Data.csv"
    cycle, currentData = readFiles(filename)
    # 对数拟合
    # popt返回的是给定模型的最优参数
    # 使用pcov的值检测拟合的质量，其对角线元素值代表着每个参数的方差。
    popt, pcov = curve_fit(func, cycle[0:100], currentData[0:100])
    # 获取popt里面是拟合系数
    #a = popt[0]
    #b = popt[1]
    return popt
    #yvals = a - b * np.log(cycle[0:100])  # 拟合y值



#忆阻器函数模型
def memristorCell(state,pulse_before,pulse_new,Conductance,popt):

    if state == 0:  #随机初始化
        Conductance = np.random.rand()
        pulse_after = 0
    elif state ==1:   #读
        Conductance = Conductance
        pulse_after = pulse_before
        pass
    elif state == 2:  #写
        pulse_after = pulse_before + pulse_new
        a = popt[0]
        b = popt[1]
        Conductance = func(pulse_after,a,b)
    return Conductance,pulse_after