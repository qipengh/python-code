# -*- coding: cp936 -*-
####################################################
#                 6.Iteration                    
#                 6.����
####################################################
# ����һ��list��tuple,��ͨ��forѭ���������list��tuple�����ֱ�����Ϊ������
# C��java�еĵ���list��ͨ���±���ɡ�����
'''
for (i = 0; i < list.length; i++){
n = list[i];
}
'''
'''
�����밴�±�����������Ĳ�ͬ�ǣ�������һ�־���ĵ���ʵ�ַ�ʽ��
��ǰ��ֻ���ĵ�����������������ĵ����ڲ������ʵ�ֵ�
'''
'''
# ������ָ����һ��Ԫ�ص����ݽṹ
1.���򼯺ϣ�list,tuple,str��unicode��
2.���򼯺ϣ�set
3.���򼯺ϲ��Ҿ���Key-Value�ԣ�dict
'''
# forѭ����������1-100����ӡ7�ı���
'''
for i in range(1,101):
    if i % 7 ==0:
        print i
'''
# ����������Python�е�����Զ��ȥ��Ԫ�ر�������Ԫ�ص�������
# ����forѭ�����õ�������������ʹ��enumerate()������
'''
��������Ҳ������İ��������ʣ������� enumerate() �����Զ���ÿ��Ԫ��
��� (index, element) ������tuple���ٵ�������ͬʱ�����������Ԫ�ر���
'''
'''
# ʹ��enumerate()������forѭ����ͬʱ��������index��Ԫ��name
# ������ÿ��Ԫ��ʵ������һ��tuple��ÿ��tupleԪ�ذ�������Ԫ�ء�
# for t in enumerate(L):
#     index = t[0]
#     name = t[1]
#     print index,'-',name  �����£�
L = ['Adam', 'Lisa', 'Paul', 'Bart']
for index,name in enumerate(L):
    print index,'-',name
    
==>
0 - Adam
1 - Lisa
2 - Paul
3 - Bart
'''
# zip()�������԰�����list���һ��list��
# zip([10, 20, 30], ['A', 'B', 'C'])==>[(10, 'A'), (20, 'B'), (30, 'C')]
# �ڵ���['Adam', 'Lisa', 'Paul', 'Bart']ʱ,��ӡ����-���֣����δ�1��ʼ��
# ʹ��zip()������range()������
'''
L = ['Adam', 'Lisa', 'Paul', 'Bart']
for index,name in zip(range(1,len(L)+1),L):
    print index,'-',name
'''
# ����dict��value��
'''
d = {'Adam' : 95,'Lisa' : 85,'Bart' : 59}
print d.values()
==>[85, 95, 59]
for v in d.values():
    print v
==>
85
95
59    
'''
# dict��values()������itervalues()�����ĵ���Ч��һ��
'''
1. values() ����ʵ���ϰ�һ�� dict ת�����˰��� value ��list��
2. ���� itervalues() ��������ת���������ڵ������������δ� dict ��ȡ�� value��
���� itervalues() ������ values() ������ʡ������ list ������ڴ档
3. ��ӡ itervalues() ����������һ�� <dictionary-valueiterator> ������˵����
Python�У�for ѭ�������õĵ�������Զ��ֹ list��tuple��str��unicode��dict�ȣ�
�κοɵ������󶼿���������forѭ�������ڲ���ε�������ͨ�������ù��ġ�

���һ������˵�Լ��ɵ����������Ǿ�ֱ���� for ѭ��ȥ��������
�ɼ���������һ�ֳ�������ݲ����������Ե��������ڲ����������κ�Ҫ��
'''
# ����һ��dict:d = {'Adam':95,'Lisa':85,'Bart':59,'Paul':74},���������ͬѧ��ƽ���֡�
'''
d = {'Adam':95,'Lisa':85,'Bart':59,'Paul':74}
sum = 0.0
for x in d.itervalues():
    sum += x
print sum / len(d)
==>78.25
'''
# ������key��value:items()����
'''
print d.items()
#==>[('Lisa', 85), ('Paul', 74), ('Adam', 95), ('Bart', 59)]
#�ɼ���items()������dict����ת�����˰���tuple��list�������list������ͬʱ���key��value
for key,value in d.items():
    print key, ':',value
# ==>
Lisa : 85
Paul : 74
Adam : 95
Bart : 59
'''
'''
�� values() ��һ�� itervalues() ���ƣ� items() Ҳ��һ����Ӧ�� iteritems()��
iteritems() ����dictת����list�������ڵ��������в��ϸ��� tuple��
���ԣ� iteritems() ��ռ�ö�����ڴ档
'''
# �����dict��d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
# ��ӡ�� name : score������ٴ�ӡ��ƽ���� average : score��
'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for k,v in d.items():
    sum += v
    print k,':',v
print 'average',':',sum / len(d)
#==>
Lisa : 85
Paul : 74
Adam : 95
Bart : 59
average : 78.25
'''
