# urllib2 ��ѧϰ֮·

# 1��urllib2 ���
# urllib2�ṩ��һ����������urlopen,ͨ����ָ����URL���������ȡ���ݡ�
# ��򵥵���ʽ���£�
'''
import urllib2
response = urllib2.urlopen('http://www.douban.com')  # 2
html = response.read()

2ʽ�ȼ���
request = urllib2.request('http://www.douban.com') # ָ��һ����������������
response = urllib2.urlopen(request) # ��������Ӧ���Կͻ��˵�����

ǰ�ԣ�
HTTP�ǻ��������Ӧ����Ƶ�--�ͻ���������󣬷�����ṩӦ��urllib2��һ��Request������ӳ���������HTTP����,
������򵥵�ʹ����ʽ���㽫����Ҫ����ĵ�ַ����һ��Request����ͨ������urlopen������Request����
������һ���������response�������Ӧ�������ͬһ���ļ����������������Response�е���.read()��
'''
# ʾ����ģ������ cookie��¼�������Ĺ��̣�
'''
import urllib, urllib2, cookielib
import bs4

# �������ĵ�¼��ַ��Ҫ��BeautifulSoup��ץȡ��
from bs4 import BeautifulSoup
url = 'http://www.renren.com/SysHome.do'

# get login url
respl = urllib2.urlopen(url)
source = respl.read()
soupl = BeautifulSoup(source)
log_url = soupl('form', {'method':'post'})[0]['action']

# login by cookie
# -info
# ������Ϣ����info�С�info��һ���ֵ�{'email':'xx','password':'xx'}.key��������Ҫ����ʵ����ҳ�ж��壬
# ���綹��Ķ�����{'form_email':'xx','form_password':'xx'}
info = {}

# -cookie
# ʹ��cookie�ĺô����ڣ���¼֮�������ʹ��cookie�б������Ϣ��Ϊͷ��Ϣ��һ���֣������Ѿ������ͷ��Ϣ���ŷ�����վ��
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

# -try log
try:
    resp2 = urllib2.urlopen(log_url, urllib.urlencode(info))
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
        print 'readon:{0}'.format(e.reason)
    if hasattr(e, 'code'):
        print 'code:{0}'.format(e.code)

'''

# 2��Data����

# ������һЩ���ݵ�URL(ͨ��URL��CGI[ͨ�����ؽӿ�]�ű���������WEBӦ�ó���ҽ�)����HTTP��,����ʹ����֪��POST�����ͣ�
# ͨ�������ύһ��HTML��ʱ�������������������������е�POSTs����Դ�ڱ������ܹ�ʹ��POST�ύ��������ݵ����Լ��ĳ���
# һ���HTML����data��Ҫ����ɱ�׼��ʽ��Ȼ����Ϊdata��������Request���󡣱��빤��ʹ��urllib�ĺ�������urllib2��
# ����ʾ�����£�
'''
import urllib
import urllib2

url = 'http://www.pythontab.com'
values = {'name' : 'Michael Foord',
          'location' : 'pythontab',
          'language' : 'Python' }
data = urllib.urlencode(values) # urlencode�������ַ����� URL ���롣
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
the_page = response.read()

>>> print data
name=Michael+Foord&language=Python&location=pythontab # URL���룺�ո��Ӻš�
'''

# 3��Headers

'''
# �������headers�����HTTP����:һЩվ�㲻ϲ�������򣨷���Ϊ���ʣ����ʣ����߷��Ͳ�ͬ�汾�����ݵ���ͬ���������
# Ĭ�ϵ�urllib2���Լ���Ϊ��Python-urllib/x.y��(x��y��Python���汾�ʹΰ汾��,����Python-urllib/2.5)��������
# ���ܻ���վ���Ի󣬻��߸ɴ಻������
# �����ȷ���Լ������ͨ��User-Agentͷ�����㴴����һ�������������Ը���һ������ͷ���ݵ��ֵ䡣
'''

# ��������ӷ��͸�����һ�������ݣ���������ģ���Internet Explorer:
'''
import urllib
import urllib2

url = 'http://www.pythontab.com'
user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
          'location' : 'pythontab',
          'language' : 'Python'}
headers = {'User_Agent' : user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
'''

# 3 Handle Exceptions�����쳣
# HTTPError��urlError�����࣬ͨ�����ض�HTTP URLs�в�����

# 3.1 URLError
# ͨ����URLError��û����������(û��·�ɵ��ض�������),���߷����������ڵ�����²�����
# ��������£��쳣ͬ�������"reason"���ԣ�����һ��tuple��������һ������ź�һ��������Ϣ��
'''
import urllib2

req = urllib2.Request('http://www.pythotab.com')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    print e.reason
>>>
[Errno 11001] getaddrinfo failed
'''

#3.2 HTTPError
