# Python 练习数据挖掘

# 四个主要的Python数据分析和处理的类库：numpy, matplotlib, sklearn, networkx.

# 数据导入和可视化
# 数据分析的覅第一步由获取数据和导入数据到我们的工作环境组成。简单的Python代码下载数据：
import urllib2

url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = urllib2.urlopen(url)
localFile = open('iris.csv','w')
localFile.write(u.read())
localFile.close()

