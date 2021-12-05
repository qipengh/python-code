# -*- coding: cp936 -*-
####################################################
#                 7.                   
#                 7.列表生成式
####################################################
# 生成列表：range();
# 而列表生成式则可以用一行语句代替循环生成上面的list：[x * x for x in range(1, 11)]
# Python特有的列表生成式:要生成的元素 x * x 放到前面，后跟 for 循环，创建出list.
'''
range(1,11)
==>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L = []
for x in range(1,11):
    L.append(x * x)
print L
==>
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 列表生成式生成列表[1*2,3*4,4*5,...,99*100]
# range(1,100,2)可生成list[1,3,5,9,...]

[x * (x+1) for x in range(1,100,2)]
'''
# 复杂表达式：
# 使用for循环可迭代普通的list，也可迭代dict。
'''
字符串可以通过 % 进行格式化，用指定的参数替代 %s。
字符串的join()方法可以把一个 list 拼接成一个字符串。
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
==>
<table border="1">
<tr><th>Name</th><th>Score</th><tr>
<tr><td>Lisa</td><td>85</td></tr>
<tr><td>Adam</td><td>95</td></tr>
<tr><td>Bart</td><td>59</td></tr>
</table>
'''
#在生成的表格中，对于没有及格的同学，请把分数标记为红色。
#提示：红色可以用 <td style="color:red"> 实现。
'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s<%td><td style = "color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
'''
# 条件过滤：
'''
[x * x for x in range(1,11) if x % 2 == 0]
==>
[4, 16, 36, 64, 100]
'''
#请编写一个函数，它接受一个 list，把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
'''
提示：
1. isinstance(x, str) 可以判断变量 x 是否是字符串；
2. 字符串的 upper() 方法可以返回大写的字母。
def toUppers(L):
	return[str.upper(x) for x in L if isinstance(x, str) == True]
print toUppers(['Hello', 'world', 101])
==>
['HELLO', 'WORLD']
'''
# 多层表达式：
'''
[m + n for m in 'ABC' for n in '123']
==>
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
该表达式相当于
L=[]
for m in 'ABC'：
    for n in '123':
        L.append(m + n)
'''
# 回文数：利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
'''
print [n1 * 100 + n2 * 10 + n3 for n1 in range(1,9) for n2 in range(0,10)
for n3 in range(0,10)if n1 == n3]
'''
