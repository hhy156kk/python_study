import urllib2

values = {"username":"385708813@qq.com",}


request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)

print response.read()
