# -*- coding: cp936 -*-

####################################################
#               2. if/else;while;for
#               2. ѡ��ṹ/�������
####################################################
"""
age = 17
if age >= 18:
    print 'adult'
else:
    print 'teenager'
"""
# ���շ������������>=90:excellent;>=80:good;>=60:passed;<60:failed
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
# ����:for��while
# ��������
'''
l = ['Adam','Lisa','Bart']
for name in l:  # name �����������forѭ���ж���ģ���˼������ȡ��list�е�ÿ��Ԫ�أ�����Ԫ�ظ�ֵ��name��Ȼ��ִ��forѭ����
    print name'''
'''#��ƽ����
l = [75,92,59,68]
sum1 = 0.0
for score in l:
    sum1 += score
print sum1 / 4'''
# ������while 100���ڵ�����,����������ͣ�
"""
sum = 0
x = 1
while x < 100:  # while���ж�x < N ʱ����ΪTrue���ͻ�����ִ����ȥ�������ѭ�����ʱ�����x += 1.����while true,if x<100,break
    if x % 2 == 1:
        print x
        sum += x
    x += 1
print sum """
# ��continue �滻:��ӡ�����100���ڵ�������
"""
sum = 0
x = 1
while True:  # while True:һֱѭ�� ֱ������break
    if x % 2 == 0:  # ��Ϊż����x��һ����������ǰѭ������ִ���������
        x += 1
        continue
    if x > 100:  # ����100��������������㣬���˳�ѭ��
        break
    sum += x  # ���
    print x
    x += 1
print sum
"""

# break ����while����ѭ�����˳���ǰѭ����
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
# ���� while true����ѭ�����break��䣬����1+2+4+8+16+��������ǰ20��ĺ�
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
# ѭ�������̣�����break�˳���ǰѭ����Ҳ����continue ��������ѭ�����룬������һ��ѭ����
# ����ƽ����
"""
L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:  # ��L�е�Ԫ�������ֵ������x�����в���
    if x < 60:  # �޳�������ĳɼ�
        continue  # ��������ѭ���ĺ�������
    sum += x  # �����ܺ�
    n += 1  # ��������һ
print sum / n  # ����ƽ����
"""
# ����ѭ�� ��ӡ
"""
for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print x + y
"""
# ����ѭ����ӡʮλ�ȸ�λС����
"""
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in l:
    for y in l:
        if x < y:
            print x * 10 + y
"""
