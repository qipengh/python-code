# -*- coding: cp936 -*-

####################################################
#                 5.Slice                    
#                 5.��Ƭ
####################################################
"""
L = ['Adam', 'Lisa', 'Paul', 'Bart']
# 5.1 L[0:3]==>['Adam', 'Lisa', 'Paul']�ȼ���L[��3]
# 5.2 L[:]==>['Adam', 'Lisa', 'Paul', 'Bart']
"""
# ��Ƭ�����ĵ���������ָÿN��ȡһ��
"""
L[::2]==>['Adam', 'Paul']
L[-2:]==>['Paul', 'Bart']
L[:-2]
L[-3:-1]
L[-4:-1:2]
"""
# ���õ�����Ƭ��1��100������ȡ�������10���������10����ı���
"""
L = range(1,101)
print L[-10:]
print L[-46::5]
"""
# ���ַ�����Ƭ
'''
'ABCDEFG'[:3]==>'ABC'
'ABCDEFG'[::2]==>'ACEG'
'''
# �ַ����еķ���upper()�ɰ��ַ���ɴ�д��ĸ��'abc'.upper()==>'ABC'
# ���һ��������������һ���ַ�����Ȼ�󷵻�һ��������ĸ��ɴ�д���ַ�����
'''
def firstCharUpper(s):
    return s.upper()
print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('septemper')
'''
