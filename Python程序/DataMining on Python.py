# Python ��ϰ�����ھ�

# �ĸ���Ҫ��Python���ݷ����ʹ������⣺numpy, matplotlib, sklearn, networkx.

# ���ݵ���Ϳ��ӻ�
# ���ݷ�����҅��һ���ɻ�ȡ���ݺ͵������ݵ����ǵĹ���������ɡ��򵥵�Python�����������ݣ�
import urllib2

url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = urllib2.urlopen(url)
localFile = open('iris.csv','w')
localFile.write(u.read())
localFile.close()

