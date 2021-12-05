# -*- coding: cp936 -*-
####################################################
#                 7.                   
#                 7.�б�����ʽ
####################################################
# �����б�range();
# ���б�����ʽ�������һ��������ѭ�����������list��[x * x for x in range(1, 11)]
# Python���е��б�����ʽ:Ҫ���ɵ�Ԫ�� x * x �ŵ�ǰ�棬��� for ѭ����������list.
'''
range(1,11)
==>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L = []
for x in range(1,11):
    L.append(x * x)
print L
==>
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# �б�����ʽ�����б�[1*2,3*4,4*5,...,99*100]
# range(1,100,2)������list[1,3,5,9,...]

[x * (x+1) for x in range(1,100,2)]
'''
# ���ӱ��ʽ��
# ʹ��forѭ���ɵ�����ͨ��list��Ҳ�ɵ���dict��
'''
�ַ�������ͨ�� % ���и�ʽ������ָ���Ĳ������ %s��
�ַ�����join()�������԰�һ�� list ƴ�ӳ�һ���ַ�����
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
==>
<table border="1">
<tr><th>Name</th><th>Score</th><tr>
<tr><td>Lisa</td><td>85</td></tr>
<tr><td>Adam</td><td>95</td></tr>
<tr><td>Bart</td><td>59</td></tr>
</table>
'''
#�����ɵı���У�����û�м����ͬѧ����ѷ������Ϊ��ɫ��
#��ʾ����ɫ������ <td style="color:red"> ʵ�֡�
'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s<%td><td style = "color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
'''
# �������ˣ�
'''
[x * x for x in range(1,11) if x % 2 == 0]
==>
[4, 16, 36, 64, 100]
'''
#���дһ��������������һ�� list����list�е������ַ�����ɴ�д�󷵻أ����ַ���Ԫ�ؽ������ԡ�
'''
��ʾ��
1. isinstance(x, str) �����жϱ��� x �Ƿ����ַ�����
2. �ַ����� upper() �������Է��ش�д����ĸ��
def toUppers(L):
	return[str.upper(x) for x in L if isinstance(x, str) == True]
print toUppers(['Hello', 'world', 101])
==>
['HELLO', 'WORLD']
'''
# �����ʽ��
'''
[m + n for m in 'ABC' for n in '123']
==>
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
�ñ��ʽ�൱��
L=[]
for m in 'ABC'��
    for n in '123':
        L.append(m + n)
'''
# ������������ 3 ��forѭ�����б�����ʽ���ҳ��ԳƵ� 3 λ�������磬121 ���ǶԳ�������Ϊ���ҵ��󵹹������� 121��
'''
print [n1 * 100 + n2 * 10 + n3 for n1 in range(1,9) for n2 in range(0,10)
for n3 in range(0,10)if n1 == n3]
'''
