#获取html网页
from urllib import request
import ssl

class Spider():
    #Target website
    url = 'https://www.panda.tv/cate/lol'

    # private method
    def __fetchContent(self):
        r  = request.urlopen(Spider.url)
        htmls = r.read()
        a = 1

    #入口方法-for private method
    def go(self):
        self.__fetchContent()

spider = Spider()
spider.go()