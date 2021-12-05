# coding: utf-8

# 黄启鹏
from numpy import *

# print(random.rand(4, 4))

# mat()函数：数组转化为矩阵
randMat = mat(random.rand(4, 4))
# .I操作符：求逆运算
print('randMat.I\n', randMat.I)

invRandMat = randMat.I
# 得到矩阵与其逆矩阵相乘
print ('randMat*invRandMat\n', randMat*invRandMat)

myEye = randMat*invRandMat
# eye(4):创建4*4的矩阵
print('myEye - eye(4)\n', myEye - eye(4))
