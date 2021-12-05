# -*- coding: utf-8 -*-

####################################################
#                 8.                   
#                 8.
####################################################

# 函数式编程的特点：
'''
1.把计算视为函数而非指令
2.纯函数式编程：不需要变量，没有副作用，测试简单。
3.支持高阶函数，代码简单。
'''

# Python支持的函数式编程：
'''
1.不是纯函数编程：允许有变量
2.支持高阶函数：函数也可作为变量传入
3.支持闭包：有了闭包就能返回函数
4.有限度地支持匿名函数
'''

#高阶函数：能接受函数做参数的函数
'''
1.变量可以指向函数:f = abs;f(-10)
函数名就是指向函数的变量:abs = len;abs([1,2,3])
2.函数的参数可以接收变量
3.一个函数可以接收另一个函数作为参数
4.能接收函数做参数的函数就是高阶函数
'''
# 例：定义一个函数，接受x,y,f三个参数：x,y是数值，f是函数。
'''
import math
def add(x,y,f):
    return f(x) + f(y)
add(-5,9,abs)
# 根号X + 根号y
print add(25, 9, math.sqrt)
'''

### 8.1 Python 内置的高阶函数map()

# 它接收一个函数f和一个list并通过把函数f依次作用在 list 的每个元素上,得到一个新的list并返回。
# 注：map()函数不改变原有的list，而是返回一个新的list。其中list包含的元素可以是任何类型
'''
def f(x):
    return x * x
print map(f,[1,2,3,4,5,6,7,8,9])
==>
[1, 4, 9, 16, 25, 36, 49, 64, 81]
'''

# ♥♥♥例题：假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，
# 请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list
'''
format_name(s)函数接收一个字符串,并且要返回格式化后的字符串,利用map()函数就可输出新的list。
def format_name(s):
    return s[0].upper() + s[1:].lower()
print map(format_name,['adam', 'LISA', 'barT'])
==>
['Adam', 'Lisa', 'Bart']
'''

### 8.2 Python 内置的高阶函数reduce()

# reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()
# 传入的函数 f必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。

# 例题1：编写一个f函数，接收x和y，返回x和y的和
'''
def f(x, y):
    return x + y
reduce(f,[1, 3, 5, 7, 9])
reduce()还可以接收第3个可选参数，作为计算的初始值。
reduce(f,[1, 3, 5, 7, 9], 100)
==>
125
因为第一轮计算是：计算初始值和第一个元素：f(100, 1)，结果为101。
'''

# 例题2：Python内置了求和函数sum()，但没有求积的函数，请利用redude()来求积
'''
def prod(x, y):
    return x * y

print reduce(prod, [2, 4, 5, 7, 12])
'''

### 8.3 Python 内置高阶函数:filter()

# filter()接收一个函数 f 和一个list。
# 这个函数 f 的作用是对每个元素进行判断，返回 True或 False，
# filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。

# 例题1：要从一个list[1,4,6,7,9,12,17]中删除偶数，保留奇数：
'''
# 先编写判断奇数的函数:
def is_odd(x):
    return x % 2 == 1
    
# 然后利用filter()过滤掉偶数：
filter(is_odd,[1,4,6,7,9,12,17])
==>
[1, 7, 9, 17]
'''

# 例题2：利用filter()，可以完成很多有用的功能，例如，删除 None 或者空字符串：
'''
def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
==>
['test', 'str', 'END']

注意: s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。
当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')，如下：

a = '     123'
a.strip()
结果： '123'

a='\t\t123\r\n'
a.strip()
结果：'123'
'''

# 例题3：请利用filter()过滤出1~100中平方根是整数的数,结果是:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
import math

def is_sqr(x):
    r = int(math.sqrt(x))
    return x and r * r == x

print filter(is_sqr, range(1, 101))
'''

### 8.4 Python中的自定义排序函数：sorted()

# Python内置的sorted()函数可对list进行排序：
'''
sorted([36, 5, 12, 9, 21])
==>
[5, 9, 12, 21, 36]
'''
# sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，
# 比较函数的定义是：传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1；
# 如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。

# 实现倒序排序，只需要编写一个reversed_cmp函数：
'''
def reversed_cmp(x, y):
    if x > y:
	return -1
    if x < y:
	return 1
    return 0

# 调用 sorted() 并传入 reversed_cmp 就可以实现倒序排序：
sorted([36, 5, 12, 9, 21],reversed_cmp)
==>
[36, 21, 12, 9, 5]
'''
# sorted()也可以对字符串进行排序，字符串默认按照ASCII大小来比较：
'''
sorted(['bob', 'about', 'Zoo', 'Credit'])
==>
['Credit', 'Zoo', 'about', 'bob']
# 'Zoo'排在'about'之前是因为'Z'的ASCII码比'a'小。
'''
# 例题：请利用sorted()高阶函数，实现忽略大小写排序的算法。
# 注：先把两个字符串都变成大写（或者都变成小写），再比较。
'''
def cmp_ignore_case(s1, s2):
    u1 = s1[0].upper()
    u2 = s2[0].upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0    

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
'''

# 8.5 Python中返回函数

# 定义一个函数f()，让它返回一个函数g:
'''
def f():
    print 'call f()...'
    # 定义函数g:
    def g():
        print 'call g()...'
    # 返回函数g:
    return g

我们在函数 f 内部又定义了一个函数g。由于函数g也是一个对象，函数名g就是指向函数 g 的变量，
所以，最外层函数f可以返回变量g，也就是函数 g 本身。调用函数f，我们会得到 f 返回的一个函数：
>>> x = f()   # 调用f()
call f()...
>>> x   # 变量x是f()返回的函数：
<function g at 0x1037bf320>
>>> x()   # x指向函数，因此可以调用
call g()...   # 调用x()就是执行g()函数定义的代码

请注意区分返回函数和返回值：
def myabs():
    return abs   # 返回函数
def myabs2(x):
    return abs(x)   # 返回函数调用的结果，返回值是一个数值
'''
# 返回函数的计算延迟执行：
'''
例如：定义一个普通的求和函数：

def calc_sum(lst):
    return sum(lst)
调用calc_sum()函数时，将立刻计算并得到结果：
>>> calc_sum([1, 2, 3, 4])
10

如果返回一个函数，就可以“延迟计算”：

def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum
    
# 调用calc_sum()并没有计算出结果，而是返回函数:
>>> f = calc_sum([1, 2, 3, 4])
>>> f
<function lazy_sum at 0x1037bfaa0>
# 对返回的函数进行调用时，才计算出结果:
>>> f()
10
'''
# ♥例题：编写函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
'''
def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod
f = calc_prod([1, 2, 3, 4])
print f()
'''

# 8.6 Python之闭包：内层函数引用了外层函数的变量，然后返回内层函数的情况。

# 在函数内部定义的函数和外部定义的函数是一样的，只是他们无法被外部访问：
'''
def g():
	print 'g()...'

def f():
	print 'f()...'
	return g
'''
# 将 g 的定义移入函数 f 内部，防止其他代码调用 g：
'''
def f():
    print 'f()...'
    def g():
        print 'g()...'
    return g
'''
'''
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum
注意: 发现没法把 lazy_sum 移到 calc_sum 的外部，因为它引用了 calc_sum 的参数 lst。
'''
# ♥像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。

# 闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，
# 就要确保引用的局部变量在函数返回后不能变.举例如下：
'''
# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果全部都是 9。

原因就是当count()函数返回了3个函数时，这3个函数所引用的变量 i 的值已经变成了3。
由于f1、f2、f3并没有被调用，所以，此时他们并未计算 i*i，当 f1 被调用时：

>>> f1()
9     # 因为f1现在才计算i*i，但现在i的值已经变为3
因此，返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''
# 返回闭包不能引用循环变量，改写count()函数，让它正确返回能计算1x1、2x2、3x3的函数。
'''
def f(j):
    def g():
        return j*j
    return g

它可以正确地返回一个闭包g，g所引用的变量j不是循环变量，因此将正常执行。

在count函数的循环内部，如果借助f函数，就可以避免引用循环变量i。    
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()   
'''
# 8.7 Python中匿名函数
'''
1、
map(lambda x:x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
==>
[1, 4, 9, 16, 25, 36, 49, 64, 81]

匿名函数lambda x: x * x 实际上就是
def f(x):
    return x * x
匿名函数是有一个限制，就是只能有一个表达式，不写return，返回值就是结果。

2、使用匿名函数，可以不必定义函数名，直接创建一个函数对象。
sorted([1, 3, 9, 5, 0],lambda x,y:-cmp(x,y))
==>
[9, 5, 3, 1, 0]

3、返回函数时，也可直接返回匿名函数：
>>> myabs = lambda x: -x if x < 0 else x
>>> myabs(-1)
1
>>> myabs(1)
1
>>> 
'''
# 使用匿名函数简化以下代码:
'''
def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

定义匿名函数时，没有return关键字，且表达式的值就是函数返回值。
>>> filter(lambda x: x and len(x.strip()) > 0,['test', None, '', 'str','  ', 'END'] )
['test', 'str', 'END']
'''
