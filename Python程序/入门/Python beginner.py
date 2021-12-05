# coding=utf-8
####################################################
#               1. list；tuple
#               1. 列表；元组
####################################################

# ···注释···
# python中的变量为动态变量，可随意赋值，即使为不同类型的变量
# "" 或 ' 或 r''' ···'''为raw字符串，其中的字符无需转义
# Unicode编码：可表示中文， u'···' 例 print u'中文'
#   coding=utf-8  （print u'中文\n日文\n韩文\n'）
# list1列表格式:
"""
l  = ['Adam',95.5,'Lisa',85,'Bart',59]
print l
"""
# list2访问列表：索引访问或是倒序访问:
"""
l = [95.5,85,59]
print l[0]+l[1]+l[2]+l[3]
print l[-1]
"""
# list3 添加元素：append（）方法：只能添加到尾部或是insert（索引号，待添加的元素）方法：排在其后的元素自动后移
"""
L = ['Adam','Lisa','Bart']
L.append('Paul')
L.insert(1,'jack')
print L
"""
# list4 删除元素：pop()方法：
"""
L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(2)
L.pop(2)
print L
"""
# list5 替换元素：直接赋值：
"""
L = ['Adam','Lisa','Bart']
L[-1] = 'Adam'
L[0] = 'Bart'
print L
"""
# tuple:t = (''):单元素tuple需自动添加一个“，”；多元素tuple无需加“,” t = ('Adam',) print t
# tuple:指向不变指的是tuple的每个元素，指向不变即指向'a'，就不能改变指向'b',
#   指向一个list，就不能指向其他对象，但指向的这个list本身是可变的。
#   要创建一个内容也不可变的tuple,就必须保证tuple的每一个元素本身也不能变。
"""
t = ('a','b',['a','b'])
print t
"""
# 注：若在Python交互环境下敲代码，还要留意缩进，并且退出缩进需要多敲一行回车

####################################################
#               2. if/else;while;for
#               2. 选择结构/控制语句
####################################################
"""
age = 17
if age >= 18:
    print 'adult'
else:
    print 'teenager'
"""
# 按照分数划定结果：>=90:excellent;>=80:good;>=60:passed;<60:failed
"""
score = 55
if score >= 90:
    print 'excellent'
elif score >=80:
    print 'good'
elif score >= 60:
    print 'passed'
else:
    print 'failed'"""
# 遍历:for、while
# 遍历姓名
'''
l = ['Adam','Lisa','Bart']
for name in l:  # name 这个变量是在for循环中定义的，意思是依次取出list中的每个元素，并把元素赋值给name，然后执行for循环体
    print name'''
'''#求平均分
l = [75,92,59,68]
sum1 = 0.0
for score in l:
    sum1 += score
print sum1 / 4'''
# 遍历：while 100以内的奇数,并输出奇数和：
"""
sum = 0
x = 1
while x < 100:  # while在判断x < N 时总是为True，就会无限执行下去，变成死循环，故必须有x += 1.或者while true,if x<100,break
    if x % 2 == 1:
        print x
        sum += x
    x += 1
print sum """
# 用continue 替换:打印并输出100以内的奇数和
"""
sum = 0
x = 1
while True:  # while True:一直循环 直到遇到break
    if x % 2 == 0:  # 若为偶数，x加一，并跳过当前循环，不执行求和运算
        x += 1
        continue
    if x > 100:  # 大于100，不进行求和运算，并退出循环
        break
    sum += x  # 求和
    print x
    x += 1
print sum
"""

# break 打破while的死循环，退出当前循环。
"""
sum = 0
x = 1
while True:
    sum += x
    x += 1
    if x >= 100:
        break
print sum
"""
# 利用 while true无限循环配合break语句，计算1+2+4+8+16+···的前20项的和
"""
sum = 0
x = 1
n = 1
while True:
    sum += x
    x *= 2
    n += 1
    if n > 20:
        break
"""
# 循环缩过程，可用break退出当前循环，也可用continue 跳过后续循环代码，继续下一次循环。
# 计算平均分
"""
L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:  # 将L中的元素逐个赋值给变量x，进行操作
    if x < 60:  # 剔除不及格的成绩
        continue  # 跳过本次循环的后续代码
    sum += x  # 计算总和
    n += 1  # 计数器加一
print sum / n  # 计算平均分
"""
# 多重循环 打印
"""
for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print x + y
"""
# 多重循环打印十位比个位小的数
"""
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in l:
    for y in l:
        if x < y:
            print x * 10 + y
"""

####################################################
#               3. dict                          ##
#               3. 数据字典                       ##
####################################################
"""d = {'key' : value}.其中len()函数表示字典长度。
查找：d[key],与list不同，list必须通过索引返回对应元素，而dict使用key
避免keyerror:
   1.判断用in:if 'Paul' in d:(\n)print d['Paul'];
   2.get()方法：print d.get('Bart')
特点：
 【1】查找速度快，list随元素增加而逐渐下降。缺点：占用内存大，浪费内存且key不可重复；list 占用内存少
 【2】存储的key-value对无顺序
 【3】作为key 的元素必须不可变
更新dict ：赋值语句直接添加即可，d['Paul'] = 72
遍历：for key in d:
"""
# 打印dict的key-value
"""
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print key, ':', d.get(key)  # print a, b, c打印abc不同于C语言的占位符。
"""
"""
d ={
    # [1, 2, 3] : 6  # 作为key的元素必须不可变。python的基本数据类型都是不可变的，都可作为key .但list是可变的，不能作为key
    '123' : [1, 2, 3],  # key 是str,value是list
    123 : '123',
    ('a', 'b') : True
}
print d
"""

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
####################################################
#                5. Classes                        #
#                5. 类                             #
####################################################
"""
class Human(object):

    # 类属性，将被这个类的所有实例所共享
    species = "H. sapiens"

    #基本的初始化函数（构造函数）
    def __init__(self, name):
        # 吧参数赋值为实例的name属性
        self.name = name

    #下面是实例方法，所有方法都以 self 为第一个参数
    def say(self, msg):
        return "%s: %s" % (self.name, msg)

    # 类方法会被所有实例共享。
    # 类方法在调用时，会将类本身作为第一个参数传入。
    @classmethod
    def get_species(cls):
        return cls.species

    # 静态方法在调用时，不会传入累或实例的引用。
    @staticmethod
    def grunt():
        return "*grunt*"

# 实例化一个类
i= Human(name="Ian")
print i.say("hi")       # 打印出 "Ian: hi"

j = Human("joel")
print j.say("hello")

# 调用我们的类方法
i.get_species()

# 修改共享属性
Human.species = "H. neanderthalensis"
i.get_species()         # =>"H.neanderthalensis"
j.get_species()

# 调用静态方法
Human.grunt()       # =>"*grunt*"
"""
####################################################
#               6. Modules                         #
#               6. 模块                            #
####################################################
# 可导入模块
"""
import math

print math.sqrt(16)

# 也可从一个模块中获取指定的函数
from math import ceil, floor
print ceil(3.7)         # => 4.0
print floor(3.7)        # => 3.0

# 可以一个模块中导入所有函数
# 警告：不建议使用这种方式
from math import *

# 可缩短模块的名称
import math as m
math.sqrt(16) ==m.sqrt(16)      # => True
"""
# Python 模块就是普通的 Python文件。
# 你可以自己编写你自己的模块，然后导入他们。
# 模块名称与文件名相同。

# 查出一个模块里有哪些函数和属性
"""
import math
dir(math)
"""