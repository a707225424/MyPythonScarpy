# -*- coding: utf-8 -*-
import scrapy
#正则
import  re
#异步提取url
from  scrapy.http import  Request
#获取域名
from urllib import  parse

from ArticeSpider.items import ArticeInfo
from ArticeSpider.items import ArticeDetial

class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['www.biqiuge.com']
    start_urls = ['https://www.biqiuge.com/book/4/']

    def parse(self, response):
        #获取小说相关信息
        ArticeInfo_re_ge = self.getArticeInfo(response)
        print(ArticeInfo_re_ge)
        #返回迭代器 需要next 循环才可以查看
        for ArticeInfo_re in ArticeInfo_re_ge:
            print (ArticeInfo_re)
            # 判断信息中是否存在对应的文章连接
            if ArticeInfo_re:
                if('articedetail' in ArticeInfo_re.keys()):
                    for  articedetail in ArticeInfo_re['articedetail']:
                        #print(articedetail[0])
                        #补全文章地址
                        #a_url = 'https://' + self.allowed_domains[0] + articedetail[0]
                        a_url = parse.urljoin(response.url, articedetail[0])
                        print(a_url)
                        #循环读取连接
                        yield scrapy.Request(url=a_url, callback=self.getArticeDetail)
                pass

        #ArticeInfo_item = ArticeInfo_re
        #yield  ArticeInfo_item

        #self.getArticeDetail(response)

        pass

    #获取小说详情 + 章节连接
    def getArticeInfo(self, response):
        # /html/body/div[5]/div[2]/h2
        # requrts = response.xpath('/html/body')

        ArticeInfo_item = ArticeInfo()
        ArticeInfo_re = {}
        # 获取名称
        title = response.xpath('//div[@class="info"]/h2/text()')
        print(title.extract()[0])
        ArticeInfo_item['title'] = title.extract()[0]

        # 获取作者等信息
        moreinfo = response.xpath('//div[@class="small"]/span').extract()
        print(moreinfo)
        more_restr = '^<span.*?>.*：(.*)</span>$'
        more_arr = []
        for i in range(0, len(moreinfo)):
            # print(moreinfo[i])
            if i != 2:
                rst = re.match(more_restr, moreinfo[i]).groups()
                print(rst[0])
                more_arr.append(rst[0])
                del rst

                pass

            pass
        ArticeInfo_item['info'] = more_arr
        print(more_arr)

        # 获取小说章节连接
        artice_url = response.css('.listmain dl').extract()
        # print(artice_url[0])
        a_restr = '.*<dt.*</dt>?(.*)'
        arst = re.match(a_restr, artice_url[0].strip().replace('\r', '').replace('\n', '').replace('\t', ''))
        if arst:
            arst = arst.groups()
            # print('```````````````')
            # print(arst[0])
            # print(arst[1])
            # 获取对应的地址 + 名称
            addres = r'.*?<dd><a href=\"(.*?)\">(.*?)<\/a><\/dd>'
            addstr = re.findall(addres, arst[0])
            ArticeInfo_item['articedetail'] = addstr
            # if addstr:
            # print('-----------')
            # for i in addstr:
            #     print('-----------')
            #     print(i)

        else:
            print('==========')

        yield ArticeInfo_item

        #yield ArticeInfo_re

        pass

    #获取章节正文内容
    def getArticeDetail(self, response):

        Detail = ArticeDetial()

        # 获取文章名称
        title = response.xpath('//h1/text()')
        print(title.extract()[0])
        Detail['title'] = title.extract()[0]

        #获取文章正文
        a_detail = response.css('#content.showtxt')
        #print(a_detail.extract()[0])
        Detail['detail'] = a_detail.extract()[0]

        #return Detail
        pass
