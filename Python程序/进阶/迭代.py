# -*- coding: cp936 -*-
####################################################
#                 6.Iteration                    
#                 6.迭代
####################################################
# 给定一个list或tuple,可通过for循环遍历这个list或tuple。这种遍历称为迭代。
# C和java中的迭代list是通过下标完成。例如
'''
for (i = 0; i < list.length; i++){
n = list[i];
}
'''
'''
迭代与按下标访问数组最大的不同是，后者是一种具体的迭代实现方式，
而前者只关心迭代结果，根本不关心迭代内部是如何实现的
'''
'''
# 集合是指包含一组元素的数据结构
1.有序集合：list,tuple,str和unicode；
2.无序集合：set
3.无序集合并且具有Key-Value对：dict
'''
# for循环迭代数列1-100并打印7的倍数
'''
for i in range(1,101):
    if i % 7 ==0:
        print i
'''
# 索引迭代：Python中迭代永远是去除元素本身，而非元素的索引。
# 想在for循环中拿到索引，方法是使用enumerate()函数。
'''
索引迭代也不是真的按索引访问，而是由 enumerate() 函数自动把每个元素
变成 (index, element) 这样的tuple，再迭代，就同时获得了索引和元素本身。
'''
'''
# 使用enumerate()函数在for循环中同时绑定了索引index和元素name
# 迭代的每个元素实际上是一个tuple，每个tuple元素包含两个元素。
# for t in enumerate(L):
#     index = t[0]
#     name = t[1]
#     print index,'-',name  简化如下：
L = ['Adam', 'Lisa', 'Paul', 'Bart']
for index,name in enumerate(L):
    print index,'-',name
    
==>
0 - Adam
1 - Lisa
2 - Paul
3 - Bart
'''
# zip()函数可以把两个list变成一个list。
# zip([10, 20, 30], ['A', 'B', 'C'])==>[(10, 'A'), (20, 'B'), (30, 'C')]
# 在迭代['Adam', 'Lisa', 'Paul', 'Bart']时,打印名次-名字（名次从1开始）
# 使用zip()函数和range()函数。
'''
L = ['Adam', 'Lisa', 'Paul', 'Bart']
for index,name in zip(range(1,len(L)+1),L):
    print index,'-',name
'''
# 迭代dict的value：
'''
d = {'Adam' : 95,'Lisa' : 85,'Bart' : 59}
print d.values()
==>[85, 95, 59]
for v in d.values():
    print v
==>
85
95
59    
'''
# dict的values()方法和itervalues()方法的迭代效果一样
'''
1. values() 方法实际上把一个 dict 转换成了包含 value 的list。
2. 但是 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，
所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存。
3. 打印 itervalues() 发现它返回一个 <dictionary-valueiterator> 对象，这说明在
Python中，for 循环可作用的迭代对象远不止 list，tuple，str，unicode，dict等，
任何可迭代对象都可以作用于for循环，而内部如何迭代我们通常并不用关心。

如果一个对象说自己可迭代，那我们就直接用 for 循环去迭代它，
可见，迭代是一种抽象的数据操作，它不对迭代对象内部的数据有任何要求。
'''
# 给定一个dict:d = {'Adam':95,'Lisa':85,'Bart':59,'Paul':74},请计算所有同学的平均分。
'''
d = {'Adam':95,'Lisa':85,'Bart':59,'Paul':74}
sum = 0.0
for x in d.itervalues():
    sum += x
print sum / len(d)
==>78.25
'''
# 迭代的key和value:items()方法
'''
print d.items()
#==>[('Lisa', 85), ('Paul', 74), ('Adam', 95), ('Bart', 59)]
#可见，items()方法把dict对象转换成了包含tuple的list，对这个list迭代可同时获得key和value
for key,value in d.items():
    print key, ':',value
# ==>
Lisa : 85
Paul : 74
Adam : 95
Bart : 59
'''
'''
和 values() 有一个 itervalues() 类似， items() 也有一个对应的 iteritems()，
iteritems() 不把dict转换成list，而是在迭代过程中不断给出 tuple，
所以， iteritems() 不占用额外的内存。
'''
# 请根据dict：d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
# 打印出 name : score，最后再打印出平均分 average : score。
'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for k,v in d.items():
    sum += v
    print k,':',v
print 'average',':',sum / len(d)
#==>
Lisa : 85
Paul : 74
Adam : 95
Bart : 59
average : 78.25
'''
