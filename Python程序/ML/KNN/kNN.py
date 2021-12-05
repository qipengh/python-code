# coding: utf-8
############################
# @time：2018.2.17
# @from: Machine Learning in Action
# @tutor: qipengh
############################

from numpy import *
import operator # 导入运算符模块，执行排序操作时使用其函数。
from numpy.ma import array


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels
group, labels = createDataSet()
print('group=\n', group)
print('labels=\n', ·    labels)

def classify0(inX, dataSet, labels, k):

    """第一部分：欧式距离计算"""
    # shape函数:查看矩阵或者数组的维数
    # c.shape[1] 为第一维的长度，c.shape[0] 为第二维的长度
    dataSetSize = dataSet.shape[0]
    # tile():重复某个数组
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffmat = diffMat**2
    sqDistances = sqDiffmat.sum(axis = 1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()

    """第二步：选择距离最小的K个点"""


