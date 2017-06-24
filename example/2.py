# -*- coding: utf-8 -*-
'''
Created on Jul 12, 2014
python 科学计算学习：numpy快速处理数据测试
@author: 皮皮
'''
import string
import matplotlib.pyplot as plt
import numpy as np


def plotDistribitionOfDegree(threshold):
    file = open("F:/Workspaces/java/stock/result/sh/distributionOfDegree/" + str(threshold) + ".csv", 'r')
    next(file)
    linesList = file.readlines()
    #     print(linesList)
    linesList = [line.strip().split(",") for line in linesList]
    file.close()
    print(linesList)
    #     years = [string.atof(x[0]) for x in linesList]
    degree = [x[0] for x in linesList]
    print(degree)
    frequency = [x[1] for x in linesList]
    print(frequency)
    plt.plot(degree, frequency, 'b*')  # ,label=$cos(x^2)$)
    plt.plot(degree, frequency, 'r')
    plt.xlabel('degree')
    plt.ylabel('frequency')
    # plt.ylim(0, 15)
    plt.title('distribution of degree (' + str(threshold) + ")")
    plt.legend()
    plt.savefig("F:/Workspaces/java/stock/result/sh/distributionOfDegree/" + str(threshold) + ".png")
    # plt.show()


if __name__ == '__main__':
    for threshold in range(5, 100, 5):
        plotDistribitionOfDegree(threshold / 100)
