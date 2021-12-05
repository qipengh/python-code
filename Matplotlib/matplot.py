"""
Matplotlib 数据处理的可视化库
From: 莫烦Python
Web:https://morvanzhou.github.io/tutorials/data-manipulation/plt/
"""

# 使用import 导入matplotlib.pyplot和numpy模块
import matplotlib.pyplot as plt
import numpy as np

''' 1.简单的线条 '''
# 使用np.linspace 定义x:范围(-1, 1),个数是50
x = np.linspace(-3, 3, 50)
# 仿真一维数据(数据)表示曲线1
y1 = 2 * x + 1
# 仿真一维数据组(x2, y2)表示曲线2
y2 = x**2

# 使用 plt.figure 定义一个图像窗口
plt.figure()
# 使用 plt.plot 画(x, y1)曲线
plt.plot(x, y1)
# 使用 plt.show 显示图像
plt.show()

# 使用plt.figure定义一个图像窗口：编号为3；大小为(8,5)
plt.figure(num=2, figsize=(8,5))
# 使用plt.plot画(x, y2)曲线
plt.plot(x, y2)
# 使用plt.plot画(x, y1)曲线，曲线的颜色属性(color)为红色；曲线的宽度为1.0；曲线类型(linestyle)为虚线
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
# 使用plt.show显示图像
plt.show()

''' 2.在matplotlib中如何设置坐标轴的范围，单位长度， 替换文字等 '''
### 调整名字和间隔

# 使用np.linspace 定义x:范围(-1, 1),个数是50
x = np.linspace(-3, 3, 50)
# 仿真一维数据(数据)表示曲线1
y1 = 2 * x + 1
# 仿真一维数据组(x2, y2)表示曲线2
y2 = x**2

# 使用plt.figure定义一个图像窗口
plt.figure(num=3, figsize=(8,5))
# 使用plt.plot画(x, y2)曲线
plt.plot(x, y2)
# 使用plt.plot画(x, y1)曲线，曲线的颜色属性(color)为红色；曲线的宽度为1.0；曲线类型(linestyle)为虚线
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
# 使用plt.xlim设置x坐标轴范围：(-1, 2)
plt.xlim((-1, 2))
# 使用plt.ylim设置y坐标轴范围：(-2, 3)
plt.ylim((-2, 3))
# 使用plt.xlabel和plt.ylibel分别设置x, y 坐标轴名称
plt.xlabel('I am x')
plt.ylabel('I am y')
# plt.show()

# 使用np.linspace 定义x:范围(-1, 2),个数是5
new_ticks = np.linspace(-1, 2, 5)
# 使用print打印出新定义的范围
print(new_ticks)
# 使用plt.xticks设置x轴刻度：范围是(-1, 2),个数是5
plt.xticks(new_ticks)
# 使用plt.xticks设置y轴刻度以及名称：刻度为[-2, -1.8, -1, 1.22, 3];
# 对应刻度的名称为[‘really bad’,’bad’,’normal’,’good’, ‘really good’]
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
plt.show()

''' 3.如何移动matplotlib 中 axis 坐标轴的位置. '''
### 设置不同的名字和位置
# 使用plt.figure定义一个图像窗口
plt.figure(num=4, figsize=(8,5))
# 使用plt.plot画(x, y2)曲线
plt.plot(x, y2)
# 使用plt.plot画(x, y1)曲线，曲线的颜色属性(color)为红色；曲线的宽度为1.0；曲线类型(linestyle)为虚线
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
# 使用plt.xlim设置x坐标轴范围：(-1, 2)
plt.xlim((-1, 2))
# 使用plt.ylim设置y坐标轴范围：(-2, 3)
plt.ylim((-2, 3))
# 使用plt.xlabel和plt.ylibel分别设置x, y 坐标轴名称

# 使用np.linspace 定义x:范围(-1, 2),个数是5
new_ticks = np.linspace(-1, 2, 5)
# 使用print打印出新定义的范围
print(new_ticks)
# 使用plt.xticks设置x轴刻度：范围是(-1, 2),个数是5
plt.xticks(new_ticks)
# 使用plt.xticks设置y轴刻度以及名称：刻度为[-2, -1.8, -1, 1.22, 3];
# 对应刻度的名称为[‘really bad’,’bad’,’normal’,’good’, ‘really good’]
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# 使用plt.gca获取当前坐标轴信息
ax = plt.gca()
# 使用.spines设置边框：右边框；使用.set_color设置边框颜色：默认白色
ax.spines['right'].set_color('none')
# 使用.spines设置边框：上边框；使用.set_color设置边框颜色：默认白色
ax.spines['top'].set_color('none')
# plt.show()

### 调整坐标轴

# 使用.xaxis.set_ticks_position设置x坐标刻度数字或是名称的位置：bottom
# 所有位置： top, bottom, both, default, none
ax.xaxis.set_ticks_position('bottom')
# 使用.spines设置边框：x轴；使用.set_position设置边框位置：y=0的位置
# 位置所有属性：outward, axes, data
ax.spines['bottom'].set_position(('data', 0))
# plt.show()

# 使用.yaxis.set_ticks_position设置y坐标刻度数字或是名称的位置：left
# 位置所有属性：outward, axes, data
ax.yaxis.set_ticks_position('left')
# 使用.spines设置边框：y轴；使用.set_position设置边框位置：x=0的位置
# 位置所有属性：outward, axes, data
ax.spines['left'].set_position(('data', 0))
plt.show()

''' 4.Legend 图例 '''
### 4.1 添加图例
# matplotlib中的legend图例就是为了展示每个数据对应的图像名称，让读者认识你的数据结构
plt.figure(num=5, figsize=(8,5))
#set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set new sticks
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# set line style
# 用变量l1, l2分别存储起来；l1, l2,要以逗号结尾，因为plt.plot()返回的是一个列表
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')
# 参数 loc='upper right' 表示图例将添加在图中的右上角.
plt.legend(loc='upper right')

### 4.2 调整位置和名称
# 要想单独修改之前的label信息，给不同类型的线条设置图例信息，可以在plt.legend输入更多的参数。如下：
plt.legend(handles=[l1, l2], labels=['up', 'down'], loc='best')
"""
# 其中’loc’参数有多种，’best’表示自动分配最佳位置，其余的如下：

 'best' : 0,
 'upper right'  : 1,
 'upper left'   : 2,
 'lower left'   : 3,
 'lower right'  : 4,
 'right'        : 5,
 'center left'  : 6,
 'center right' : 7,
 'lower center' : 8,
 'upper center' : 9,
 'center'       : 10,
"""
plt.show()
