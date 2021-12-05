# -*- coding: utf-8 -*-

####################################################
#                9.                         
#                9. 装饰器                           
####################################################
# 定义了一个函数，想在运行时动态增加功能，又不想改动函数本身的代码
# 示例：想对以下函数增加log功能，打印出函数调用：
'''
def f1(x):
    return x*2
def f2():
    return x*x
def f3():
    return x*x*x
'''
# 方法一：给每个函数增加print'call f1()/f2()/f3()'
# 方法二：通过高阶函数返回新函数：
'''
def f1(x):
    return x*2
def new_fn(f): # 装饰器函数
    def fn(x):
        print 'call' + f.__name__ + '()'
        return f(x)
    return fn
# g1 = new_fn(f1)
# print g1(5)

f1 = new_fn(f1)
print f1(5) # f1的原始定义被彻底隐藏了
'''
# Python内置的@语法就是为了简化装饰器调用
'''
@new_fn
def f1(x):
    return x * 2
等价于
def f1(x):
    return x*2
f1 = new_fn(f1)    
'''
# 装饰器的作用：
'''
1、可以极大地简化代码，避免每个函数编写重复性代码
   打印日志：@log
   检测性能：@performance
   数据库事务：@transaction
   URL路由:@post('/register')
'''

# 1、编写无参数decorator
'''
# 考察一个log的定义
def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn

对于参数不是一个的函数，调用将报错：

@log
def add(x, y):
    return x + y
print add(1, 2)
因为 add() 函数需要传入两个参数，但是 @log 写死了只含一个参数的返回函数。
'''
#要让 @log 自适应任何参数定义的函数，可以利用Python的 *args 和 **kw，保证任意个数的参数总是能正常调用：
'''
def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn
'''
# 任务：编写一个@performance，它可以打印出函数调用的时间。计算函数调用的时间可以记录调用前后的当前时间戳，然后计算两个时间戳的差。
'''
import time
def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in %fs' % (f.__name__, (t2 - t1))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
'''

# 2、编写带参数decorator

# 由上节装饰器
'''
def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
'''
# 由于其打印语句不能变，故传入以下参数：
'''
@log('DEBUG')
def my_func():
    pass

my_func = log('DEBUG')(my_func)

# 上式展开如下：
log_decorator = log('DEBUG')
my_func = log_decorator(my_func)

# 上面的语句又相当于：
log_decorator = log('DEBUG')
@log_decorator
def my_func():
    pass
'''
'''
因此，带参数的log函数首先返回一个decorator函数，再让这个decorator函数
接收my_func并返回新函数：

def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()
'''
# 例题：上一节的@performance只能打印秒，请给 @performace 增加一个参数，允许传入's'或'ms'：
'''
要实现带参数的@performance，就需要实现：
my_func = performance('ms')(my_func)
需要3层嵌套的decorator来实现。

参考代码:

import time
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

'''

# @decorator可以动态实现函数功能的增加，但是，经过@decorator“改造”后的函数，和原函数相比，除了功能多一点外，有没有其它不同的地方？
'''
@decorator可以动态实现函数功能的增加，但是，经过@decorator“改造”后的函数，和原函数相比，除了功能多一点外，有没有其它不同的地方？

在没有decorator的情况下，打印函数名：

def f1(x):
    pass
print f1.__name__
输出： f1

有decorator的情况下，再打印函数名：

def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
@log
def f2(x):
    pass
print f2.__name__
输出： wrapper

可见，由于decorator返回的新函数函数名已经不是'f2'，而是@log内部定义的'wrapper'。这对于那些依赖函数名的代码就会失效。decorator还改变了函数的__doc__等其它属性。如果要让调用者看不出一个函数经过了@decorator的“改造”，就需要把原函数的一些属性复制到新函数中：

def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper
这样写decorator很不方便，因为我们也很难把原函数的所有必要属性都一个一个复制到新函数上，所以Python内置的functools可以用来自动化完成这个“复制”的任务：

import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
最后需要指出，由于我们把原函数签名改成了(*args, **kw)，因此，无法获得原函数的原始参数信息。即便我们采用固定参数来装饰只有一个参数的函数：

def log(f):
    @functools.wraps(f)
    def wrapper(x):
        print 'call...'
        return f(x)
    return wrapper
也可能改变原函数的参数名，因为新函数的参数名始终是 'x'，原函数定义的参数名不一定叫 'x'。
'''

# 任务：请思考带参数的@decorator，@functools.wraps应该放置在哪：

'''
注意@functools.wraps应该作用在返回的新函数上。

参考代码:

import time, functools
def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial.__name__
'''


