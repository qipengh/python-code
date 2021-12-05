# -*- coding: cp936 -*-


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
