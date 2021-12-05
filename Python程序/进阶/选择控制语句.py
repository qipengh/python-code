# -*- coding: cp936 -*-

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
