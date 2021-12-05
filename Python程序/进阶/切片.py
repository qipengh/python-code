# -*- coding: cp936 -*-

####################################################
#                 5.Slice                    
#                 5.切片
####################################################
"""
L = ['Adam', 'Lisa', 'Paul', 'Bart']
# 5.1 L[0:3]==>['Adam', 'Lisa', 'Paul']等价于L[：3]
# 5.2 L[:]==>['Adam', 'Lisa', 'Paul', 'Bart']
"""
# 切片操作的第三个参数指每N个取一个
"""
L[::2]==>['Adam', 'Paul']
L[-2:]==>['Paul', 'Bart']
L[:-2]
L[-3:-1]
L[-4:-1:2]
"""
# 利用倒序切片对1—100的数列取出：最后10个数；最后10个五的倍数
"""
L = range(1,101)
print L[-10:]
print L[-46::5]
"""
# 对字符串切片
'''
'ABCDEFG'[:3]==>'ABC'
'ABCDEFG'[::2]==>'ACEG'
'''
# 字符串中的方法upper()可把字符变成大写字母：'abc'.upper()==>'ABC'
# 设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。
'''
def firstCharUpper(s):
    return s.upper()
print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('septemper')
'''
