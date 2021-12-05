# -*- coding: cp936 -*-
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
