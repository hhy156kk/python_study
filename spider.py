#_*_ coding: utf-8_*_
import urllib
import urllib2
import re

page = 2
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)

content = response.read().decode('utf-8')
print content
pattern = re.compile(r'<div.*?class="content">(.*?)</div>', re.S)
items = re.findall(pattern, content)
for item in items:
    print item
