import re

from urllib import request

class chickenDinner():

    #target website
    url = "https://live.bilibili.com/p/eden/area-tags?parentAreaId=3&areaId=153&visit_id=66kel2wjuccg#/3/153"
    rootPattern = 'class="info">([/s/S]*?)</div>'
    rootName = ''


    def __fetchContent(self):
        r = request.urlopen(chickenDinner.url)

        htmls = r.read()
        return str(htmls, encoding='utf-8')

    def __analysis(self, html):
        root = re.findall(chickenDinner.rootPattern, html)
        anchors = []
        for html in root:





    def go(self):
        html = self.__fetchContent()






test = chickenDinner()
test.go()
