code123
首页 业界 创业 面试 Java Python
 提交
分分钟学会一门语言之Python篇
作者：code123|时间：2015-08-20|浏览：51,392 views|分类：Python
Python 是 90 年代初由 Guido Van Rossum 创立的。它是当前最流行的程序语言之一。它那纯净的语法令我一见倾心，它简直就是可以运行的伪码。

请注意：本文以 Python 2.7 为基准，但也应该适用于所有 2.X 版本。还要继续学习最新的 Python 3 哦！


# Single line comments start with a hash.
# 单行注释由一个井号开头。
""" Multiline strings can be written
    using three "'s, and are often used
    as comments
    三个双引号（或单引号）之间可以写多行字符串，
    通常用来写注释。
"""

####################################################
## 1. Primitive Datatypes and Operators
## 1. 基本数据类型和操作符
####################################################

# You have numbers
# 数字就是数字
3 #=> 3

# Math is what you would expect
# 四则运算也是你所期望的那样
1 + 1 #=> 2
8 - 1 #=> 7
10 * 2 #=> 20
35 / 5 #=> 7

# Division is a bit tricky. It is integer division and floors the results
# automatically.
# 除法有一点棘手。
# 对于整数除法来说，计算结果会自动取整。
5 / 2 #=> 2

# To fix division we need to learn about floats.
# 为了修正除法的问题，我们需要先学习浮点数。
2.0     # This is a float
2.0     # 这是一个浮点数
11.0 / 4.0 #=> 2.75 ahhh...much better
11.0 / 4.0 #=> 2.75 啊……这样就好多了

# Enforce precedence with parentheses
# 使用小括号来强制计算的优先顺序
(1 + 3) * 2 #=> 8

# Boolean values are primitives
# 布尔值也是基本数据类型
True
False

# negate with not
# 使用 not 来取反
not True #=> False
not False #=> True

# Equality is ==
# 等式判断用 ==
1 == 1 #=> True
2 == 1 #=> False

# Inequality is !=
# 不等式判断是用 !=
1 != 1 #=> False
2 != 1 #=> True

# More comparisons
# 还有更多的比较运算
1 < 10 #=> True
1 > 10 #=> False
2 <= 2 #=> True
2 >= 2 #=> True

# Comparisons can be chained!
# 居然可以把比较运算串连起来！
1 < 2 < 3 #=> True
2 < 3 < 2 #=> False

# Strings are created with " or '
# 使用 " 或 ' 来创建字符串
"This is a string."
'This is also a string.'

# Strings can be added too!
# 字符串也可以相加！
"Hello " + "world!" #=> "Hello world!"

# A string can be treated like a list of characters
# 一个字符串可以视为一个字符的列表
# （译注：后面会讲到“列表”。）
"This is a string"[0] #=> 'T'

# % can be used to format strings, like this:
# % 可以用来格式化字符串，就像这样：
"%s can be %s" % ("strings", "interpolated")

# A newer way to format strings is the format method.
# This method is the preferred way
# 后来又有一种格式化字符串的新方法：format 方法。
# 我们推荐使用这个方法。
"{0} can be {1}".format("strings", "formatted")

# You can use keywords if you don't want to count.
# 如果你不喜欢数数的话，可以使用关键字（变量）。
"{name} wants to eat {food}".format(name="Bob", food="lasagna")

# None is an object
# None 是一个对象
None #=> None

# Don't use the equality `==` symbol to compare objects to None
# Use `is` instead
# 不要使用相等符号 `==` 来把对象和 None 进行比较，
# 而要用 `is`。
"etc" is None #=> False
None is None  #=> True

# The 'is' operator tests for object identity. This isn't
# very useful when dealing with primitive values, but is
# very useful when dealing with objects.
# 这个 `is` 操作符用于比较两个对象的标识。
# （译注：对象一旦建立，其标识就不会改变，可以认为它就是对象的内存地址。）
# 在处理基本数据类型时基本用不上，
# 但它在处理对象时很有用。

# None, 0, and empty strings/lists all evaluate to False.
# All other values are True
# None、0 以及空字符串和空列表都等于 False，
# 除此以外的所有值都等于 True。
0 == False  #=> True
"" == False #=> True


####################################################
## 2. Variables and Collections
## 2. 变量和集合
####################################################

# Printing is pretty easy
# 打印输出很简单
print "I'm Python. Nice to meet you!"


# No need to declare variables before assigning to them.
# 在赋值给变量之前不需要声明
some_var = 5    # Convention is to use lower_case_with_underscores
                # 变量名的约定是使用下划线分隔的小写单词
some_var #=> 5

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
# 访问一个未赋值的变量会产生一个异常。
# 进一步了解异常处理，可参见下一节《控制流》。
some_other_var  # Raises a name error
                # 会抛出一个名称错误

# if can be used as an expression
# if 可以作为表达式来使用
"yahoo!" if 3 > 2 else 2 #=> "yahoo!"

# Lists store sequences
# 列表用于存储序列
li = []
# You can start with a prefilled list
# 我们先尝试一个预先填充好的列表
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
# 使用 append 方法把元素添加到列表的尾部
li.append(1)    #li is now [1]
                #li 现在是 [1]
li.append(2)    #li is now [1, 2]
                #li 现在是 [1, 2]
li.append(4)    #li is now [1, 2, 4]
                #li 现在是 [1, 2, 4]
li.append(3)    #li is now [1, 2, 4, 3]
                #li 现在是 [1, 2, 4, 3]
# Remove from the end with pop
# 使用 pop 来移除最后一个元素
li.pop()        #=> 3 and li is now [1, 2, 4]
                #=> 3，然后 li 现在是 [1, 2, 4]
# Let's put it back
# 我们再把它放回去
li.append(3)    # li is now [1, 2, 4, 3] again.
                # li 现在又是 [1, 2, 4, 3] 了

# Access a list like you would any array
# 像访问其它语言的数组那样访问列表
li[0] #=> 1
# Look at the last element
# 查询最后一个元素
li[-1] #=> 3

# Looking out of bounds is an IndexError
# 越界查询会产生一个索引错误
li[4] # Raises an IndexError
      # 抛出一个索引错误

# You can look at ranges with slice syntax.
# (It's a closed/open range for you mathy types.)
# 你可以使用切片语法来查询列表的一个范围。
# （这个范围相当于数学中的左闭右开区间。）
li[1:3] #=> [2, 4]
# Omit the beginning
# 省略开头
li[2:] #=> [4, 3]
# Omit the end
# 省略结尾
li[:3] #=> [1, 2, 4]

# Remove arbitrary elements from a list with del
# 使用 del 来删除列表中的任意元素
del li[2] # li is now [1, 2, 3]
          # li 现在是 [1, 2, 3]

# You can add lists
# 可以把列表相加
li + other_li #=> [1, 2, 3, 4, 5, 6] - Note: li and other_li is left alone
              #=> [1, 2, 3, 4, 5, 6] - 请留意 li 和 other_li 并不会被修改

# Concatenate lists with extend
# 使用 extend 来合并列表
li.extend(other_li) # Now li is [1, 2, 3, 4, 5, 6]
                    # 现在 li 是 [1, 2, 3, 4, 5, 6]

# Check for existence in a list with in
# 用 in 来检查是否存在于某个列表中
1 in li #=> True

# Examine the length with len
# 用 len 来检测列表的长度
len(li) #=> 6


# Tuples are like lists but are immutable.
# 元组很像列表，但它是“不可变”的。
tup = (1, 2, 3)
tup[0] #=> 1
tup[0] = 3  # Raises a TypeError
            # 抛出一个类型错误

# You can do all those list thingies on tuples too
# 操作列表的方式通常也能用在元组身上
len(tup) #=> 3
tup + (4, 5, 6) #=> (1, 2, 3, 4, 5, 6)
tup[:2] #=> (1, 2)
2 in tup #=> True

# You can unpack tuples (or lists) into variables
# 你可以把元组（或列表）中的元素解包赋值给多个变量
a, b, c = (1, 2, 3)     # a is now 1, b is now 2 and c is now 3
                        # 现在 a 是 1，b 是 2，c 是 3
# Tuples are created by default if you leave out the parentheses
# 如果你省去了小括号，那么元组会被自动创建
d, e, f = 4, 5, 6
# Now look how easy it is to swap two values
# 再来看看交换两个值是多么简单。
e, d = d, e     # d is now 5 and e is now 4
                # 现在 d 是 5 而 e 是 4


# Dictionaries store mappings
# 字典用于存储映射关系
empty_dict = {}
# Here is a prefilled dictionary
# 这是一个预先填充的字典
filled_dict = {"one": 1, "two": 2, "three": 3}

# Look up values with []
# 使用 [] 来查询键值
filled_dict["one"] #=> 1

# Get all keys as a list
# 将字典的所有键名获取为一个列表
filled_dict.keys() #=> ["three", "two", "one"]
# Note - Dictionary key ordering is not guaranteed.
# Your results might not match this exactly.
# 请注意：无法保证字典键名的顺序如何排列。
# 你得到的结果可能跟上面的示例不一致。

# Get all values as a list
# 将字典的所有键值获取为一个列表
filled_dict.values() #=> [3, 2, 1]
# Note - Same as above regarding key ordering.
# 请注意：顺序的问题和上面一样。

# Check for existence of keys in a dictionary with in
# 使用 in 来检查一个字典是否包含某个键名
"one" in filled_dict #=> True
1 in filled_dict #=> False

# Looking up a non-existing key is a KeyError
# 查询一个不存在的键名会产生一个键名错误
filled_dict["four"] # KeyError
                    # 键名错误

# Use get method to avoid the KeyError
# 所以要使用 get 方法来避免键名错误
filled_dict.get("one") #=> 1
filled_dict.get("four") #=> None
# The get method supports a default argument when the value is missing
# get 方法支持传入一个默认值参数，将在取不到值时返回。
filled_dict.get("one", 4) #=> 1
filled_dict.get("four", 4) #=> 4

# Setdefault method is a safe way to add new key-value pair into dictionary
# Setdefault 方法可以安全地把新的名值对添加到字典里
filled_dict.setdefault("five", 5) #filled_dict["five"] is set to 5
                                  #filled_dict["five"] 被设置为 5
filled_dict.setdefault("five", 6) #filled_dict["five"] is still 5
                                  #filled_dict["five"] 仍然为 5


# Sets store ... well sets
# set 用于保存集合
empty_set = set()
# Initialize a set with a bunch of values
# 使用一堆值来初始化一个集合
some_set = set([1,2,2,3,4]) # some_set is now set([1, 2, 3, 4])
                            # some_set 现在是 set([1, 2, 3, 4])

# Since Python 2.7, {} can be used to declare a set
# 从 Python 2.7 开始，{} 可以用来声明一个集合
filled_set = {1, 2, 2, 3, 4} # => {1, 2, 3, 4}
                             # （译注：集合是种无序不重复的元素集，因此重复的 2 被滤除了。）
                             # （译注：{} 不会创建一个空集合，只会创建一个空字典。）

# Add more items to a set
# 把更多的元素添加进一个集合
filled_set.add(5) # filled_set is now {1, 2, 3, 4, 5}
                  # filled_set 现在是 {1, 2, 3, 4, 5}

# Do set intersection with &
# 使用 & 来获取交集
other_set = {3, 4, 5, 6}
filled_set & other_set #=> {3, 4, 5}

# Do set union with |
# 使用 | 来获取并集
filled_set | other_set #=> {1, 2, 3, 4, 5, 6}

# Do set difference with -
# 使用 - 来获取补集
{1,2,3,4} - {2,3,5} #=> {1, 4}

# Check for existence in a set with in
# 使用 in 来检查是否存在于某个集合中
2 in filled_set #=> True
10 in filled_set #=> False


####################################################
## 3. Control Flow
## 3. 控制流
####################################################

# Let's just make a variable
# 我们先创建一个变量
some_var = 5

# Here is an if statement. Indentation is significant in python!
# prints "some_var is smaller than 10"
# 这里有一个条件语句。缩进在 Python 中可是很重要的哦！
# 程序会打印出 "some_var is smaller than 10"
# （译注：意为“some_var 比 10 小”。）
if some_var > 10:
    print "some_var is totally bigger than 10."
    # （译注：意为“some_var 完全比 10 大”。）
elif some_var < 10:    # This elif clause is optional.
                       # 这里的 elif 子句是可选的
    print "some_var is smaller than 10."
    # （译注：意为“some_var 比 10 小”。）
else:           # This is optional too.
                # 这一句也是可选的
    print "some_var is indeed 10."
    # （译注：意为“some_var 就是 10”。）


"""
For loops iterate over lists
for 循环可以遍历列表
prints:
如果要打印出：
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # You can use % to interpolate formatted strings
    # 别忘了你可以使用 % 来格式化字符串
    print "%s is a mammal" % animal
    # （译注：意为“%s 是哺乳动物”。）

"""
`range(number)` returns a list of numbers
from zero to the given number
`range(数字)` 会返回一个数字列表，
这个列表将包含从零到给定的数字。
prints:
如果要打印出：
    0
    1
    2
    3
"""
for i in range(4):
    print i

"""
While loops go until a condition is no longer met.
while 循环会一直继续，直到条件不再满足。
prints:
如果要打印出：
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print x
    x += 1  # Shorthand for x = x + 1
            # 这是 x = x + 1 的简写方式

# Handle exceptions with a try/except block
# 使用 try/except 代码块来处理异常

# Works on Python 2.6 and up:
# 适用于 Python 2.6 及以上版本：
try:
    # Use raise to raise an error
    # 使用 raise 来抛出一个错误
    raise IndexError("This is an index error")
    # 抛出一个索引错误：“这是一个索引错误”。
except IndexError as e:
    pass    # Pass is just a no-op. Usually you would do recovery here.
            # pass 只是一个空操作。通常你应该在这里做一些恢复工作。


####################################################
## 4. Functions
## 4. 函数
####################################################

# Use def to create new functions
# 使用 def 来创建新函数
def add(x, y):
    print "x is %s and y is %s" % (x, y)
    # （译注：意为“x 是 %s 而且 y 是 %s”。）
    return x + y    # Return values with a return statement
                    # 使用 return 语句来返回值

# Calling functions with parameters
# 调用函数并传入参数
add(5, 6) #=> prints out "x is 5 and y is 6" and returns 11
          # （译注：意为“x 是 5 而且 y 是 6”，并返回 11）

# Another way to call functions is with keyword arguments
# 调用函数的另一种方式是传入关键字参数
add(y=6, x=5)   # Keyword arguments can arrive in any order.
                # 关键字参数可以以任意顺序传入

# You can define functions that take a variable number of
# positional arguments
# 你可以定义一个函数，并让它接受可变数量的定位参数。
def varargs(*args):
    return args

varargs(1, 2, 3) #=> (1,2,3)


# You can define functions that take a variable number of
# keyword arguments, as well
# 你也可以定义一个函数，并让它接受可变数量的关键字参数。
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
# 我们试着调用它，看看会发生什么：
keyword_args(big="foot", loch="ness") #=> {"big": "foot", "loch": "ness"}

# You can do both at once, if you like
# 你还可以同时使用这两类参数，只要你愿意：
def all_the_args(*args, **kwargs):
    print args
    print kwargs
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# When calling functions, you can do the opposite of varargs/kwargs!
# Use * to expand tuples and use ** to expand kwargs.
# 在调用函数时，定位参数和关键字参数还可以反过来用。
# 使用 * 来展开元组，使用 ** 来展开关键字参数。
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args) # equivalent to foo(1, 2, 3, 4)
                    # 相当于 all_the_args(1, 2, 3, 4)
all_the_args(**kwargs) # equivalent to foo(a=3, b=4)
                       # 相当于 all_the_args(a=3, b=4)
all_the_args(*args, **kwargs) # equivalent to foo(1, 2, 3, 4, a=3, b=4)
                              # 相当于 all_the_args(1, 2, 3, 4, a=3, b=4)

# Python has first class functions
# 函数在 Python 中是一等公民
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3) #=> 13

# There are also anonymous functions
# 还有匿名函数
(lambda x: x > 2)(3) #=> True

# There are built-in higher order functions
# 还有一些内建的高阶函数
map(add_10, [1,2,3]) #=> [11, 12, 13]
filter(lambda x: x > 5, [3, 4, 5, 6, 7]) #=> [6, 7]

# We can use list comprehensions for nice maps and filters
# 我们可以使用列表推导式来模拟 map 和 filter
[add_10(i) for i in [1, 2, 3]]  #=> [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5] #=> [6, 7]

####################################################
## 5. Classes
## 5. 类
####################################################

# We subclass from object to get a class.
# 我们可以从对象中继承，来得到一个类。
class Human(object):

    # A class attribute. It is shared by all instances of this class
    # 下面是一个类属性。它将被这个类的所有实例共享。
    species = "H. sapiens"

    # Basic initializer
    # 基本的初始化函数（构造函数）
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        # 把参数赋值为实例的 name 属性
        self.name = name

    # An instance method. All methods take self as the first argument
    # 下面是一个实例方法。所有方法都以 self 作为第一个参数。
    def say(self, msg):
       return "%s: %s" % (self.name, msg)

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    # 类方法会被所有实例共享。
    # 类方法在调用时，会将类本身作为第一个函数传入。
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    # 静态方法在调用时，不会传入类或实例的引用。
    @staticmethod
    def grunt():
        return "*grunt*"


# Instantiate a class
# 实例化一个类
i = Human(name="Ian")
print i.say("hi")     # prints out "Ian: hi"
                      # 打印出 "Ian: hi"

j = Human("Joel")
print j.say("hello")  # prints out "Joel: hello"
                      # 打印出 "Joel: hello"

# Call our class method
# 调用我们的类方法
i.get_species() #=> "H. sapiens"

# Change the shared attribute
# 修改共享属性
Human.species = "H. neanderthalensis"
i.get_species() #=> "H. neanderthalensis"
j.get_species() #=> "H. neanderthalensis"

# Call the static method
# 调用静态方法
Human.grunt() #=> "*grunt*"


####################################################
## 6. Modules
## 6. 模块
####################################################

# You can import modules
# 你可以导入模块
import math
print math.sqrt(16) #=> 4

# You can get specific functions from a module
# 也可以从一个模块中获取指定的函数
from math import ceil, floor
print ceil(3.7)  #=> 4.0
print floor(3.7) #=> 3.0

# You can import all functions from a module.
# Warning: this is not recommended
# 你可以从一个模块中导入所有函数
# 警告：不建议使用这种方式
from math import *

# You can shorten module names
# 你可以缩短模块的名称
import math as m
math.sqrt(16) == m.sqrt(16) #=> True

# Python modules are just ordinary python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.
# Python 模块就是普通的 Python 文件。
# 你可以编写你自己的模块，然后导入它们。
# 模块的名称与文件名相同。

# You can find out which functions and attributes
# defines a module.
# 你可以查出一个模块里有哪些函数和属性
import math
dir(math)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
# Single line comments start with a hash.
# 单行注释由一个井号开头。
""" Multiline strings can be written
    using three "'s, and are often used
    as comments
    三个双引号（或单引号）之间可以写多行字符串，
    通常用来写注释。
"""

####################################################
## 1. Primitive Datatypes and Operators
## 1. 基本数据类型和操作符
####################################################

# You have numbers
# 数字就是数字
3 #=> 3

# Math is what you would expect
# 四则运算也是你所期望的那样
1 + 1 #=> 2
8 - 1 #=> 7
10 * 2 #=> 20
35 / 5 #=> 7

# Division is a bit tricky. It is integer division and floors the results
# automatically.
# 除法有一点棘手。
# 对于整数除法来说，计算结果会自动取整。
5 / 2 #=> 2

# To fix division we need to learn about floats.
# 为了修正除法的问题，我们需要先学习浮点数。
2.0     # This is a float
2.0     # 这是一个浮点数
11.0 / 4.0 #=> 2.75 ahhh...much better
11.0 / 4.0 #=> 2.75 啊……这样就好多了

# Enforce precedence with parentheses
# 使用小括号来强制计算的优先顺序
(1 + 3) * 2 #=> 8

# Boolean values are primitives
# 布尔值也是基本数据类型
True
False

# negate with not
# 使用 not 来取反
not True #=> False
not False #=> True

# Equality is ==
# 等式判断用 ==
1 == 1 #=> True
2 == 1 #=> False

# Inequality is !=
# 不等式判断是用 !=
1 != 1 #=> False
2 != 1 #=> True

# More comparisons
# 还有更多的比较运算
1 < 10 #=> True
1 > 10 #=> False
2 <= 2 #=> True
2 >= 2 #=> True

# Comparisons can be chained!
# 居然可以把比较运算串连起来！
1 < 2 < 3 #=> True
2 < 3 < 2 #=> False

# Strings are created with " or '
# 使用 " 或 ' 来创建字符串
"This is a string."
'This is also a string.'

# Strings can be added too!
# 字符串也可以相加！
"Hello " + "world!" #=> "Hello world!"

# A string can be treated like a list of characters
# 一个字符串可以视为一个字符的列表
# （译注：后面会讲到“列表”。）
"This is a string"[0] #=> 'T'

# % can be used to format strings, like this:
# % 可以用来格式化字符串，就像这样：
"%s can be %s" % ("strings", "interpolated")

# A newer way to format strings is the format method.
# This method is the preferred way
# 后来又有一种格式化字符串的新方法：format 方法。
# 我们推荐使用这个方法。
"{0} can be {1}".format("strings", "formatted")

# You can use keywords if you don't want to count.
# 如果你不喜欢数数的话，可以使用关键字（变量）。
"{name} wants to eat {food}".format(name="Bob", food="lasagna")

# None is an object
# None 是一个对象
None #=> None

# Don't use the equality `==` symbol to compare objects to None
# Use `is` instead
# 不要使用相等符号 `==` 来把对象和 None 进行比较，
# 而要用 `is`。
"etc" is None #=> False
None is None  #=> True

# The 'is' operator tests for object identity. This isn't
# very useful when dealing with primitive values, but is
# very useful when dealing with objects.
# 这个 `is` 操作符用于比较两个对象的标识。
# （译注：对象一旦建立，其标识就不会改变，可以认为它就是对象的内存地址。）
# 在处理基本数据类型时基本用不上，
# 但它在处理对象时很有用。

# None, 0, and empty strings/lists all evaluate to False.
# All other values are True
# None、0 以及空字符串和空列表都等于 False，
# 除此以外的所有值都等于 True。
0 == False  #=> True
"" == False #=> True


####################################################
## 2. Variables and Collections
## 2. 变量和集合
####################################################

# Printing is pretty easy
# 打印输出很简单
print "I'm Python. Nice to meet you!"


# No need to declare variables before assigning to them.
# 在赋值给变量之前不需要声明
some_var = 5    # Convention is to use lower_case_with_underscores
                # 变量名的约定是使用下划线分隔的小写单词
some_var #=> 5

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
# 访问一个未赋值的变量会产生一个异常。
# 进一步了解异常处理，可参见下一节《控制流》。
some_other_var  # Raises a name error
                # 会抛出一个名称错误

# if can be used as an expression
# if 可以作为表达式来使用
"yahoo!" if 3 > 2 else 2 #=> "yahoo!"

# Lists store sequences
# 列表用于存储序列
li = []
# You can start with a prefilled list
# 我们先尝试一个预先填充好的列表
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
# 使用 append 方法把元素添加到列表的尾部
li.append(1)    #li is now [1]
                #li 现在是 [1]
li.append(2)    #li is now [1, 2]
                #li 现在是 [1, 2]
li.append(4)    #li is now [1, 2, 4]
                #li 现在是 [1, 2, 4]
li.append(3)    #li is now [1, 2, 4, 3]
                #li 现在是 [1, 2, 4, 3]
# Remove from the end with pop
# 使用 pop 来移除最后一个元素
li.pop()        #=> 3 and li is now [1, 2, 4]
                #=> 3，然后 li 现在是 [1, 2, 4]
# Let's put it back
# 我们再把它放回去
li.append(3)    # li is now [1, 2, 4, 3] again.
                # li 现在又是 [1, 2, 4, 3] 了

# Access a list like you would any array
# 像访问其它语言的数组那样访问列表
li[0] #=> 1
# Look at the last element
# 查询最后一个元素
li[-1] #=> 3

# Looking out of bounds is an IndexError
# 越界查询会产生一个索引错误
li[4] # Raises an IndexError
      # 抛出一个索引错误

# You can look at ranges with slice syntax.
# (It's a closed/open range for you mathy types.)
# 你可以使用切片语法来查询列表的一个范围。
# （这个范围相当于数学中的左闭右开区间。）
li[1:3] #=> [2, 4]
# Omit the beginning
# 省略开头
li[2:] #=> [4, 3]
# Omit the end
# 省略结尾
li[:3] #=> [1, 2, 4]

# Remove arbitrary elements from a list with del
# 使用 del 来删除列表中的任意元素
del li[2] # li is now [1, 2, 3]
          # li 现在是 [1, 2, 3]

# You can add lists
# 可以把列表相加
li + other_li #=> [1, 2, 3, 4, 5, 6] - Note: li and other_li is left alone
              #=> [1, 2, 3, 4, 5, 6] - 请留意 li 和 other_li 并不会被修改

# Concatenate lists with extend
# 使用 extend 来合并列表
li.extend(other_li) # Now li is [1, 2, 3, 4, 5, 6]
                    # 现在 li 是 [1, 2, 3, 4, 5, 6]

# Check for existence in a list with in
# 用 in 来检查是否存在于某个列表中
1 in li #=> True

# Examine the length with len
# 用 len 来检测列表的长度
len(li) #=> 6


# Tuples are like lists but are immutable.
# 元组很像列表，但它是“不可变”的。
tup = (1, 2, 3)
tup[0] #=> 1
tup[0] = 3  # Raises a TypeError
            # 抛出一个类型错误

# You can do all those list thingies on tuples too
# 操作列表的方式通常也能用在元组身上
len(tup) #=> 3
tup + (4, 5, 6) #=> (1, 2, 3, 4, 5, 6)
tup[:2] #=> (1, 2)
2 in tup #=> True

# You can unpack tuples (or lists) into variables
# 你可以把元组（或列表）中的元素解包赋值给多个变量
a, b, c = (1, 2, 3)     # a is now 1, b is now 2 and c is now 3
                        # 现在 a 是 1，b 是 2，c 是 3
# Tuples are created by default if you leave out the parentheses
# 如果你省去了小括号，那么元组会被自动创建
d, e, f = 4, 5, 6
# Now look how easy it is to swap two values
# 再来看看交换两个值是多么简单。
e, d = d, e     # d is now 5 and e is now 4
                # 现在 d 是 5 而 e 是 4


# Dictionaries store mappings
# 字典用于存储映射关系
empty_dict = {}
# Here is a prefilled dictionary
# 这是一个预先填充的字典
filled_dict = {"one": 1, "two": 2, "three": 3}

# Look up values with []
# 使用 [] 来查询键值
filled_dict["one"] #=> 1

# Get all keys as a list
# 将字典的所有键名获取为一个列表
filled_dict.keys() #=> ["three", "two", "one"]
# Note - Dictionary key ordering is not guaranteed.
# Your results might not match this exactly.
# 请注意：无法保证字典键名的顺序如何排列。
# 你得到的结果可能跟上面的示例不一致。

# Get all values as a list
# 将字典的所有键值获取为一个列表
filled_dict.values() #=> [3, 2, 1]
# Note - Same as above regarding key ordering.
# 请注意：顺序的问题和上面一样。

# Check for existence of keys in a dictionary with in
# 使用 in 来检查一个字典是否包含某个键名
"one" in filled_dict #=> True
1 in filled_dict #=> False

# Looking up a non-existing key is a KeyError
# 查询一个不存在的键名会产生一个键名错误
filled_dict["four"] # KeyError
                    # 键名错误

# Use get method to avoid the KeyError
# 所以要使用 get 方法来避免键名错误
filled_dict.get("one") #=> 1
filled_dict.get("four") #=> None
# The get method supports a default argument when the value is missing
# get 方法支持传入一个默认值参数，将在取不到值时返回。
filled_dict.get("one", 4) #=> 1
filled_dict.get("four", 4) #=> 4

# Setdefault method is a safe way to add new key-value pair into dictionary
# Setdefault 方法可以安全地把新的名值对添加到字典里
filled_dict.setdefault("five", 5) #filled_dict["five"] is set to 5
                                  #filled_dict["five"] 被设置为 5
filled_dict.setdefault("five", 6) #filled_dict["five"] is still 5
                                  #filled_dict["five"] 仍然为 5


# Sets store ... well sets
# set 用于保存集合
empty_set = set()
# Initialize a set with a bunch of values
# 使用一堆值来初始化一个集合
some_set = set([1,2,2,3,4]) # some_set is now set([1, 2, 3, 4])
                            # some_set 现在是 set([1, 2, 3, 4])

# Since Python 2.7, {} can be used to declare a set
# 从 Python 2.7 开始，{} 可以用来声明一个集合
filled_set = {1, 2, 2, 3, 4} # => {1, 2, 3, 4}
                             # （译注：集合是种无序不重复的元素集，因此重复的 2 被滤除了。）
                             # （译注：{} 不会创建一个空集合，只会创建一个空字典。）

# Add more items to a set
# 把更多的元素添加进一个集合
filled_set.add(5) # filled_set is now {1, 2, 3, 4, 5}
                  # filled_set 现在是 {1, 2, 3, 4, 5}

# Do set intersection with &
# 使用 & 来获取交集
other_set = {3, 4, 5, 6}
filled_set & other_set #=> {3, 4, 5}

# Do set union with |
# 使用 | 来获取并集
filled_set | other_set #=> {1, 2, 3, 4, 5, 6}

# Do set difference with -
# 使用 - 来获取补集
{1,2,3,4} - {2,3,5} #=> {1, 4}

# Check for existence in a set with in
# 使用 in 来检查是否存在于某个集合中
2 in filled_set #=> True
10 in filled_set #=> False


####################################################
## 3. Control Flow
## 3. 控制流
####################################################

# Let's just make a variable
# 我们先创建一个变量
some_var = 5

# Here is an if statement. Indentation is significant in python!
# prints "some_var is smaller than 10"
# 这里有一个条件语句。缩进在 Python 中可是很重要的哦！
# 程序会打印出 "some_var is smaller than 10"
# （译注：意为“some_var 比 10 小”。）
if some_var > 10:
    print "some_var is totally bigger than 10."
    # （译注：意为“some_var 完全比 10 大”。）
elif some_var < 10:    # This elif clause is optional.
                       # 这里的 elif 子句是可选的
    print "some_var is smaller than 10."
    # （译注：意为“some_var 比 10 小”。）
else:           # This is optional too.
                # 这一句也是可选的
    print "some_var is indeed 10."
    # （译注：意为“some_var 就是 10”。）


"""
For loops iterate over lists
for 循环可以遍历列表
prints:
如果要打印出：
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # You can use % to interpolate formatted strings
    # 别忘了你可以使用 % 来格式化字符串
    print "%s is a mammal" % animal
    # （译注：意为“%s 是哺乳动物”。）

"""
`range(number)` returns a list of numbers
from zero to the given number
`range(数字)` 会返回一个数字列表，
这个列表将包含从零到给定的数字。
prints:
如果要打印出：
    0
    1
    2
    3
"""
for i in range(4):
    print i

"""
While loops go until a condition is no longer met.
while 循环会一直继续，直到条件不再满足。
prints:
如果要打印出：
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print x
    x += 1  # Shorthand for x = x + 1
            # 这是 x = x + 1 的简写方式

# Handle exceptions with a try/except block
# 使用 try/except 代码块来处理异常

# Works on Python 2.6 and up:
# 适用于 Python 2.6 及以上版本：
try:
    # Use raise to raise an error
    # 使用 raise 来抛出一个错误
    raise IndexError("This is an index error")
    # 抛出一个索引错误：“这是一个索引错误”。
except IndexError as e:
    pass    # Pass is just a no-op. Usually you would do recovery here.
            # pass 只是一个空操作。通常你应该在这里做一些恢复工作。


####################################################
## 4. Functions
## 4. 函数
####################################################

# Use def to create new functions
# 使用 def 来创建新函数
def add(x, y):
    print "x is %s and y is %s" % (x, y)
    # （译注：意为“x 是 %s 而且 y 是 %s”。）
    return x + y    # Return values with a return statement
                    # 使用 return 语句来返回值

# Calling functions with parameters
# 调用函数并传入参数
add(5, 6) #=> prints out "x is 5 and y is 6" and returns 11
          # （译注：意为“x 是 5 而且 y 是 6”，并返回 11）

# Another way to call functions is with keyword arguments
# 调用函数的另一种方式是传入关键字参数
add(y=6, x=5)   # Keyword arguments can arrive in any order.
                # 关键字参数可以以任意顺序传入

# You can define functions that take a variable number of
# positional arguments
# 你可以定义一个函数，并让它接受可变数量的定位参数。
def varargs(*args):
    return args

varargs(1, 2, 3) #=> (1,2,3)


# You can define functions that take a variable number of
# keyword arguments, as well
# 你也可以定义一个函数，并让它接受可变数量的关键字参数。
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
# 我们试着调用它，看看会发生什么：
keyword_args(big="foot", loch="ness") #=> {"big": "foot", "loch": "ness"}

# You can do both at once, if you like
# 你还可以同时使用这两类参数，只要你愿意：
def all_the_args(*args, **kwargs):
    print args
    print kwargs
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# When calling functions, you can do the opposite of varargs/kwargs!
# Use * to expand tuples and use ** to expand kwargs.
# 在调用函数时，定位参数和关键字参数还可以反过来用。
# 使用 * 来展开元组，使用 ** 来展开关键字参数。
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args) # equivalent to foo(1, 2, 3, 4)
                    # 相当于 all_the_args(1, 2, 3, 4)
all_the_args(**kwargs) # equivalent to foo(a=3, b=4)
                       # 相当于 all_the_args(a=3, b=4)
all_the_args(*args, **kwargs) # equivalent to foo(1, 2, 3, 4, a=3, b=4)
                              # 相当于 all_the_args(1, 2, 3, 4, a=3, b=4)

# Python has first class functions
# 函数在 Python 中是一等公民
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3) #=> 13

# There are also anonymous functions
# 还有匿名函数
(lambda x: x > 2)(3) #=> True

# There are built-in higher order functions
# 还有一些内建的高阶函数
map(add_10, [1,2,3]) #=> [11, 12, 13]
filter(lambda x: x > 5, [3, 4, 5, 6, 7]) #=> [6, 7]

# We can use list comprehensions for nice maps and filters
# 我们可以使用列表推导式来模拟 map 和 filter
[add_10(i) for i in [1, 2, 3]]  #=> [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5] #=> [6, 7]

####################################################
## 5. Classes
## 5. 类
####################################################

# We subclass from object to get a class.
# 我们可以从对象中继承，来得到一个类。
class Human(object):

    # A class attribute. It is shared by all instances of this class
    # 下面是一个类属性。它将被这个类的所有实例共享。
    species = "H. sapiens"

    # Basic initializer
    # 基本的初始化函数（构造函数）
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        # 把参数赋值为实例的 name 属性
        self.name = name

    # An instance method. All methods take self as the first argument
    # 下面是一个实例方法。所有方法都以 self 作为第一个参数。
    def say(self, msg):
       return "%s: %s" % (self.name, msg)

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    # 类方法会被所有实例共享。
    # 类方法在调用时，会将类本身作为第一个函数传入。
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    # 静态方法在调用时，不会传入类或实例的引用。
    @staticmethod
    def grunt():
        return "*grunt*"


# Instantiate a class
# 实例化一个类
i = Human(name="Ian")
print i.say("hi")     # prints out "Ian: hi"
                      # 打印出 "Ian: hi"

j = Human("Joel")
print j.say("hello")  # prints out "Joel: hello"
                      # 打印出 "Joel: hello"

# Call our class method
# 调用我们的类方法
i.get_species() #=> "H. sapiens"

# Change the shared attribute
# 修改共享属性
Human.species = "H. neanderthalensis"
i.get_species() #=> "H. neanderthalensis"
j.get_species() #=> "H. neanderthalensis"

# Call the static method
# 调用静态方法
Human.grunt() #=> "*grunt*"


####################################################
## 6. Modules
## 6. 模块
####################################################

# You can import modules
# 你可以导入模块
import math
print math.sqrt(16) #=> 4

# You can get specific functions from a module
# 也可以从一个模块中获取指定的函数
from math import ceil, floor
print ceil(3.7)  #=> 4.0
print floor(3.7) #=> 3.0

# You can import all functions from a module.
# Warning: this is not recommended
# 你可以从一个模块中导入所有函数
# 警告：不建议使用这种方式
from math import *

# You can shorten module names
# 你可以缩短模块的名称
import math as m
math.sqrt(16) == m.sqrt(16) #=> True

# Python modules are just ordinary python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.
# Python 模块就是普通的 Python 文件。
# 你可以编写你自己的模块，然后导入它们。
# 模块的名称与文件名相同。

# You can find out which functions and attributes
# defines a module.
# 你可以查出一个模块里有哪些函数和属性
import math
dir(math)


Source File: adambard/learnxinyminutes-docs - GitHub

Translated by: cssmagic

