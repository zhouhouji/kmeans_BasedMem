#测试函数，用于实践一些不确定的东西
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def readFiles(filename):
    rawData = pd.read_csv(filename)
    cycle = rawData.iloc[:, 0].values
    currentData = rawData.iloc[:, 1].values
    return cycle, currentData


def drawScatter(plt, data_X, data_Y, size, color, mrkr):
    plt.scatter(data_X.tolist(), data_Y.tolist(), s=size, c=color, marker=mrkr)


# 自定义函数 e指数形式
def func(x, a, b):
    return a - b * np.log(x)


if __name__ == '__main__':
    # 打开的文件名
    filename = "LiSiO_Data.csv"
    cycle, currentData = readFiles(filename)

    drawScatter(plt, cycle, currentData, size=60, color='black', mrkr='o')
    plt.show()

    '''
    #多项式拟合
    f1 = np.polyfit(cycle[0:100], currentData[0:100], 3)
    p1 = np.poly1d(f1)
    print(p1)
    yvals = p1(cycle[0:100])  # 拟合y值


    # 指数拟合

    popt, pcov = curve_fit(func, cycle[0:100], currentData[0:100])
    # 获取popt里面是拟合系数
    a = popt[0]
    b = popt[1]

    yvals = func(cycle[0:100], a, b)  # 拟合y值
    print (u'系数a:', a)
    print (u'系数b:', b)
    '''

    # 对数拟合
    # popt返回的是给定模型的最优参数
    # 使用pcov的值检测拟合的质量，其对角线元素值代表着每个参数的方差。
    popt, pcov = curve_fit(func, cycle[0:100], currentData[0:100])
    # 获取popt里面是拟合系数
    a = popt[0]
    b = popt[1]
    yvals = a - b * np.log(cycle[0:100])  # 拟合y值
    print(u'系数', popt)
    print(u'拟合效果', pcov)

    # 绘图
    plot1 = plt.plot(cycle[0:100], currentData[0:100], 's', label='original values')
    plot2 = plt.plot(cycle[0:100], yvals, 'r', label='polyfit values')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc=1)  # 指定legend的位置右上角
    plt.title('polyfitting')
    plt.show()
