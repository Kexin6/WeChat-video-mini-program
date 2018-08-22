'''
    This is a module
'''

import re

#获取html网页
from urllib import request


class Spider():
    '''
        This is a class
    '''
    #Target website
    url = 'https://www.panda.tv/cate/lol'

    #正则表达式定位tag *选取全部 ？非贪婪
    rootPattern = '<div class="video-info">([\s\S]*?)</div>'
    rootName = '</i>([\s\S]*?)</span>'
    rootNumber = '<span class="video-number">([\d\D]*?)</span>'

    # private method
    def __fetchContent(self):
        #http request
        r  = request.urlopen(Spider.url)

        #htmls return bytes
        htmls = r.read()
        return str(htmls, encoding='utf-8')

    #正则分析
    def __analysis(self, htmls):
        root = re.findall(spider.rootPattern, htmls)
        anchors = []
        for html in root:
            name = re.findall(spider.rootName, html)
            number = re.findall(spider.rootNumber, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors


    def __refine(self, anchors):
        '''
            #数据精炼
            #去掉空格，且把列表变为str
        '''
        l = lambda anchor: {'name':anchor['name'][0].strip(),
                           'number':anchor['number'][0]
                           }
        return map(l, anchors)

    #业务处理
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sortSeed, reverse=True)
        return anchors

    def __sortSeed(self, anchors):
        r = re.findall('\d*', anchors['number'])
        number = float(r[0])
        if '万' in anchors['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('rank' + str(rank + 1) + ':' + anchors[rank]['name'] + '------' + anchors[rank]['number'])


    def go(self):
        '''
            入口方法-for private method即总方法
        '''
        htmls = self.__fetchContent()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)

spider = Spider()
spider.go()