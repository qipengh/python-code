#coding:utf-8
# 使用import 导入matplotlib.pyplot和numpy模块
import matplotlib.pyplot as plt
import numpy as np


''' 1.简单的线条 '''
# 使用np.linspace 定义x:范围(-1, 1),个数是50
# x = np.linspace(-3, 3, 50)
# 仿真一维数据(数据)表示贪婪剪枝策略
x1 = [38.68, 48.52, 57.90, 62.20, 65.35, 67.36, 67.80, 70.67]
y1 = [85.37, 84.81, 84.77, 84.18, 84.24, 84.02, 83.94, 83.93]

# 仿真一维数据组(x2, y2)表示动态网络手术
x2 = [37.97, 41.25, 44.71, 47.65, 50.33, 57.41, 62.18, 67.17, 71.12]
y2 = [85.25, 84.85, 84.88, 84.84, 84.67, 84.37, 83.85, 83.72, 83.64]

# 使用plt.figure定义一个图像窗口
fig = plt.figure(num=3, figsize=(8,5))
# 使用plt.xlim设置x坐标轴范围：(-1, 2)
plt.xlim((35, 75))
# 使用plt.ylim设置y坐标轴范围：(-2, 3)
plt.ylim((82, 90))
# 使用plt.xlabel和plt.ylibel分别设置x, y 坐标轴名称
plt.xlabel(u'剪枝比例(%)')
plt.ylabel(u'模型准确率(%)')
plt.title(u'两种剪枝策略得到的稀疏模型对比')
# set line style
# 用变量l1, l2分别存储起来；l1, l2,要以逗号结尾，因为plt.plot()返回的是一个列表
l1, = plt.plot(x1, y1, label=u'贪婪剪枝策略')
l2, = plt.plot(x2, y2, color='red', linewidth=1.0, linestyle='--', label=u'动态网络手术')
# 参数 loc='upper right' 表示图例将添加在图中的右上角.
plt.legend(loc='upper right')

# 绘制小图
x = [1, 2, 3]
y = [79.19, 82.36, 83.88]
# 4个值都是占整个figure坐标系的百分比。
# 假设figure的大小是10x10，那么小图就被包含在由(2, 5.5)开始，宽2.5，高2.5的坐标系内。
left, bottom, width, height = 0.2, 0.55, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x, y, 'b')
ax2.set_xlabel(u'训练次数(万次)')
ax2.set_ylabel(u'准确率(%)')
ax2.set_title('原始模型')

plt.show()
