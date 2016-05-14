import urllib2
import urllib

data={}
data['word']='Jecvay Notes'

url_values = urllib.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_values


response = urllib2.urlopen(full_url)
print response.read()
