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

    def __init__(self,baseUrl,seeLZ,pn):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.pageIndex ='&pn='+str(pn)
        self.tool = Tool()

    def getPage(self,url):
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')

    def getTitle(self,page):
        pattern = re.compile(r"<h3.*?>(.*?)</h3>",re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip().encode('utf-8')
        else:
            return None

    def getPageNum(self,page):
        pattern = re.compile(r'<li class="l_reply_num.*?</span>.*?<span class="red">(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getContent(self,page):
        pattern = re.compile(r'<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    def start(self):
        url = self.baseURL + self.seeLZ + self.pageIndex
        page = self.getPage(url)
        title = self.getTitle(page)
        pageNum = self.getPageNum(page)
        contents = self.getContent(page)
        print "帖子标题: " + str(title)
        print "帖子页数：" + str(pageNum)
        for content in contents:
            print content

baseURL = "http://tieba.baidu.com/p/3138733512?"
seeLZ = raw_input("是否之收看楼主")
pn = raw_input("帖子页码")

bdtbSpider = BDTB(baseURL,seeLZ,pn)
bdtbSpider.start()
