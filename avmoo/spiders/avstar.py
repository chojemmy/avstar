# -*- coding: utf-8 -*-
import scrapy
from ..items import AvmooItem


class AvstarSpider(scrapy.Spider):
    name = 'avstar'
    
    @property
    def start_urls(self):
        url_tmpl = 'https://avmoo.xyz/cn/actresses/page/{}'

        return(url_tmpl.format(i) for i in range(1,206))

    def parse(self, response):
        for avstar in response.xpath('//div[@class="item"]'):
            item = AvmooItem()

            item['name'] = avstar.xpath('.//div[@class="photo-info"]/span/text()').extract_first()
            avstar_url = response.urljoin(avstar.xpath('.//a/@href').extract_first())

            request = scrapy.Request(avstar_url, callback=self.parse_starinfo)

            request.meta['item'] = item

            yield request

    def parse_starinfo(self, response):

        item = response.meta['item']

        item['birthday'] = response.xpath('//div[@class="avatar-box"]').xpath('.//p/text()').re_first('生日: (.+)')

        item['height'] = response.xpath('//div[@class="avatar-box"]').xpath('//p/text()').re_first('身高: (.+)cm')

        yield item

