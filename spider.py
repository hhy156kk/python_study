# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class QSBK_Spider:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent':self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self,pageIndex):
        url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
        request = urllib2.Request(url,headers=self.headers)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        pattern = re.compile('<div.*?class="content">(.*?)</div>',re.S)
        items = re.findall(pattern,pageCode)
        pageStories = []
        for item in items:
            pageStories.append(item)
        return pageStories

   def loadPage(self):
       if self.enable == True:
           if len(self.stories)<2:
               pageStories = self.getPageItems(self.pageIndex)
               self.stories.append(pageStories)
               self.pageIndex += 1


    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == 'Q'
                self.enable = False
                return
            print

    def start(self):
        print u'正在读取糗事百科,按回车查看新段子，Q退出'
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QSBK_Spider()
spider.start()
