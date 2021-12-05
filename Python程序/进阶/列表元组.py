# -*- coding: cp936 -*-


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
