# -*- coding:utf-8 -*-
import  urllib2
import  urllib
import  re

class Tool:

    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')


    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.replacePara,"",x)
        return x.strip()

class BDTB:

    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()

    def getPage(self,pageNum):
        try:
            url = self.baseURL + self.seeLZ
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"百度贴吧链接失败，错误原因"+e.reason
                return None
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile(r"<h3.*?>(.*?)</h3>",re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile(r'<li class="l_reply_num.*?</span>.*?<span class="red">(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getContent(self):
        page = self.getPage(1)
        pattern = re.compile(r'<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
            print content
        return contents


baseUrl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl,1)
#bdtb.getTitle()
#bdtb.getPageNum()
bdtb.getContent()
