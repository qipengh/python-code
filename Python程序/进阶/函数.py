# -*- coding: cp936 -*-


####################################################
#               4. Functions
#               4. ����
####################################################
# ʹ��def��������
"""
def add(x, y):
    print "x is %s and y is %s" % (x, y)
    return x + y
add(3, 5)
"""

# ���庯����ʹ�����ܿɱ������Ķ�λ����
"""
def varargs(*args):
    return args

print varargs(1, 2, 3)
"""
# ����һ��������������һ��list������list��ÿ��Ԫ��ƽ���ĺ�
"""
def square_of_sum(L):
    sum = 0
    for i in L:
        sum += i*i
    return sum
print square_of_sum([1,2,3,4,5])
print square_of_sum([-5,0,5,15,25])
"""
# Python����֮���ض�ֵ
# math���ṩ��sin()��cos()��������Ҫ��import����
"""
import math
def move(x,y,step,angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
# x,y = move(100,100,60,math.pi / 6)
# print x,y
r = move(100,100,60,math.pi / 6) 
print r # ���ص���һ��tuple.��ʵPython�ĺ������ض�ֵ���Ƿ���һ��tuple��
"""
# һԪ���η��̣�ax*x+bx+c=0.��д��������һԪ���η��̵�������
"""
import math
def quadratic_equation(a,b,c):
    x1 = ((-b) + math.sqrt(b*b - 4*a*c))/(2*a) # ��������Python�б�ʾ�б���������
    x2 = ((-b) - math.sqrt(b*b - 4*a*c))/(2*a)
    return x1,x2
print quadratic_equation(2,3,0)
print quadratic_equation(1,-6,5)

"""
# Python֮�ݹ麯����һ���������ڲ���������
# ʹ�õݹ麯��һ��Ҫ��ֹջ������ڼ�����У�����������ͨ��ջ��stack���������ݽṹʵ�ֵġ�
# ÿ������һ���������ã�ջ�ͻ��һ��ջ֡��ÿ���������أ�ջ�ͻ��һ��ջ֡��
# ����ջ�Ĵ�С�������޴�ģ����Եݹ���õĴ������࣬�ᵼ��ջ�����
# �׳˺���fact(n):n!=1*2*3*4*...*(n-1)*n
"""
def fact(n):
    if n==1:
	return 1
    return n * fact(n-1)
"""
# ��ŵ�����ƶ�
"""
# coding=utf-8
def move(n,a,b,c):
    if n==1:  
        print a,'-->',c   
    else:  
        move(n-1,a,c,b)   #��ǰn-1�����Ӵ�a�ƶ���b��  
        move(1,a,b,c)     #������µ����һ�����Ӵ�a�ƶ���c��  
        move(n-1,b,a,c)   #��b�ϵ�n-1�������ƶ���c��
move(4,'A','B','C')
"""
