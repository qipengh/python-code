# -*- coding:utf-8 -*-
import numpy as np
from sklearn import model_selection, svm
import pandas as pd


# 从csv文件中读取数据集
df = pd.read_csv('breast-cancer-wisconsin.data.csv')
# 在处理数据之前获取一些统计信息
df.describe()
# 在“Bland Chromatin”列中有一些值丢失了，我们将用列的平均值替换它们
df.replace('?', 3, inplace=True)
# 展示我们的数据集的前五个示例
df.head()
# 显示数据集信息
df.info()
# 删除id列，因为它没有提供任何信息
df.drop(['id'], 1, inplace=True)
# 显示删除后的数据样式
df.head()

# 将X设置为特征矩阵
X = np.array(df.drop(['Class'], 1))
# 将Y设置为标签向量
y = np.array(df['Class'])

# 确保已得到正确的数组
print(X.shape, y.shape)
print("----\nX:")
print(X)
print("----\ny:")
print(y[:10])

# 将数据集划分为训练集和交叉验证集
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

# 创建支持向量Clasifier
clf = svm.SVC()
# 将它与数据集相匹配
clf.fit(X_train, y_train)

# 训练了SVM分类器之后，显示准确性
accuracy = clf.score(X_test, y_test)
print("Accuracy: " + str(round(accuracy*100, 2)) + "%")

