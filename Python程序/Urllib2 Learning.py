# urllib2 的学习之路

# 1、urllib2 简介
# urllib2提供了一个基础函数urlopen,通过向指定的URL发送请求获取数据。
# 最简单的形式如下：
'''
import urllib2
response = urllib2.urlopen('http://www.douban.com')  # 2
html = response.read()

2式等价于
request = urllib2.request('http://www.douban.com') # 指定一个域名并发送请求。
response = urllib2.urlopen(request) # 服务器响应来自客户端的请求。

前言：
HTTP是基于请求和应答机制的--客户端提出请求，服务端提供应答。urllib2用一个Request对象来映射你提出的HTTP请求,
在它最简单的使用形式中你将用你要请求的地址创建一个Request对象，通过调用urlopen并传入Request对象，
将返回一个相关请求response对象，这个应答对象如同一个文件对象，所以你可以在Response中调用.read()。
'''
# 示例：模拟利用 cookie登录人人网的过程：
'''
import urllib, urllib2, cookielib
import bs4

# 人人网的登录地址需要用BeautifulSoup来抓取。
from bs4 import BeautifulSoup
url = 'http://www.renren.com/SysHome.do'

# get login url
respl = urllib2.urlopen(url)
source = respl.read()
soupl = BeautifulSoup(source)
log_url = soupl('form', {'method':'post'})[0]['action']

# login by cookie
# -info
# 个人信息存在info中。info是一个字典{'email':'xx','password':'xx'}.key的命名需要根据实际网页中定义，
# 比如豆瓣的定义是{'form_email':'xx','form_password':'xx'}
info = {}

# -cookie
# 使用cookie的好处在于，登录之后你可以使用cookie中保存的信息作为头信息的一部分，利用已经保存的头信息接着访问网站。
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

# 2、Data数据

# 当发送一些数据到URL(通常URL与CGI[通用网关接口]脚本，或其他WEB应用程序挂接)。在HTTP中,经常使用熟知的POST请求发送，
# 通常在你提交一个HTML表单时由你的浏览器来做。并不是所有的POSTs都来源于表单，你能够使用POST提交任意的数据到你自己的程序。
# 一般的HTML表单，data需要编码成标准形式。然后做为data参数传到Request对象。编码工作使用urllib的函数而非urllib2。
# 代码示例如下：
'''
import urllib
import urllib2

url = 'http://www.pythontab.com'
values = {'name' : 'Michael Foord',
          'location' : 'pythontab',
          'language' : 'Python' }
data = urllib.urlencode(values) # urlencode函数将字符串以 URL 编码。
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
the_page = response.read()

>>> print data
name=Michael+Foord&language=Python&location=pythontab # URL编码：空格变加号。
'''

# 3、Headers

'''
# 怎样添加headers到你的HTTP请求:一些站点不喜欢被程序（非人为访问）访问，或者发送不同版本的内容到不同的浏览器。
# 默认的urllib2把自己作为“Python-urllib/x.y”(x和y是Python主版本和次版本号,例如Python-urllib/2.5)，这个身份
# 可能会让站点迷惑，或者干脆不工作。
# 浏览器确认自己身份是通过User-Agent头，当你创建了一个请求对象，你可以给他一个包含头数据的字典。
'''

# 下面的例子发送跟上面一样的内容，但把自身模拟成Internet Explorer:
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

# 3 Handle Exceptions处理异常
# HTTPError是urlError的子类，通常在特定HTTP URLs中产生。

# 3.1 URLError
# 通常，URLError在没有网络连接(没有路由到特定服务器),或者服务器不存在的情况下产生。
# 这种情况下，异常同样会带有"reason"属性，它是一个tuple，包含了一个错误号和一个错误信息。
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
