import urllib2
import urllib

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

values = {"username":"385708813@qq.com", "password":"hhy156kk"}
headers = {'User-Agent':user_agent,'Referer':'http://www.zhihu.com/articles'}

data = urllib.urlencode(values)

request = urllib2.Request(url,data,headers)

response = urllib2.urlopen(request)

print response.read()
