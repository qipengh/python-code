# -*- coding: cp936 -*-


####################################################
#               4. Functions
#               4. 函数
####################################################
# 使用def创建函数
"""
def add(x, y):
    print "x is %s and y is %s" % (x, y)
    return x + y
add(3, 5)
"""

# 定义函数，使他接受可变数量的定位参数
"""
def varargs(*args):
    return args

print varargs(1, 2, 3)
"""
# 定义一个函数，它接受一个list，返回list中每个元素平方的和
"""
def square_of_sum(L):
    sum = 0
    for i in L:
        sum += i*i
    return sum
print square_of_sum([1,2,3,4,5])
print square_of_sum([-5,0,5,15,25])
"""
# Python函数之返回多值
# math包提供了sin()和cos()函数。需要用import引用
"""
import math
def move(x,y,step,angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
# x,y = move(100,100,60,math.pi / 6)
# print x,y
r = move(100,100,60,math.pi / 6) 
print r # 返回的是一个tuple.其实Python的函数返回多值就是返回一个tuple。
"""
# 一元二次方程：ax*x+bx+c=0.编写函数返回一元二次方程的两个解
"""
import math
def quadratic_equation(a,b,c):
    x1 = ((-b) + math.sqrt(b*b - 4*a*c))/(2*a) # 中括号在Python中表示列表，不可乱用
    x2 = ((-b) - math.sqrt(b*b - 4*a*c))/(2*a)
    return x1,x2
print quadratic_equation(2,3,0)
print quadratic_equation(1,-6,5)

"""
# Python之递归函数：一个函数在内部调用自身。
# 使用递归函数一定要防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的。
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限大的，所以递归调用的次数过多，会导致栈溢出。
# 阶乘函数fact(n):n!=1*2*3*4*...*(n-1)*n
"""
def fact(n):
    if n==1:
	return 1
    return n * fact(n-1)
"""
# 汉诺塔的移动
"""
# coding=utf-8
def move(n,a,b,c):
    if n==1:  
        print a,'-->',c   
    else:  
        move(n-1,a,c,b)   #将前n-1个盘子从a移动到b上  
        move(1,a,b,c)     #将最底下的最后一个盘子从a移动到c上  
        move(n-1,b,a,c)   #将b上的n-1个盘子移动到c上
move(4,'A','B','C')
"""
