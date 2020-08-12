import scrapy
import re
from .shops import Shops


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    stats = Shops.config

    def start_requests(self):
        search = getattr(self, 'search', None)
        if search:
            for shop_name, shop_stats in self.stats.items():
                self.shop = shop_name
                url = shop_stats['base_page'] + shop_stats['brandlist']
                if shop_name == 'wildberries':
                    letter = search[0].lower()
                    url += letter
                yield scrapy.Request(url, callback=self.pre_parse)

    def pre_parse(self, response):
        shop = self.shop
        stats = Shops.config[shop]
        url = stats['base_page']
        search = self.search.lower()
        for brand in response.css(stats['brand']):
            title = brand.css(stats['brand_title']).get().lower()
            if search == title:
                link = brand.css(stats['brand_link']).get() + '/all'
                url += link
                break
        if url == stats['base_page']:
            url += f"{stats['default_search']}{search}"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        shop = self.shop
        stats = Shops.config[shop]
        for quote in response.css(stats['item']):
            if self.shop == 'lamoda':
                prices = [quote.css(stats[i]).get() for i in (
                    'item_price_act', 'item_price_new', 'item_price')]
                price = min(re.sub('^ +', "", i) for i in prices if i)
                print(f'---------------{prices}---------------')
                self.price = f"{price}{quote.css(stats['currency']).get()}"
                self.link = stats['base_page']
            else:
                price = quote.css(stats['item_price']).get()
                self.price = price
                self.link = ''
            yield {
                'price': self.price,
                'brand name': re.sub('\n +', "", quote.css(stats['item_brand']).get()),
                'specification': re.sub('\n +', "", quote.css(stats['item_spec']).get()),
                'link': f"{self.link}{quote.css(stats['item_link']).get()}"
            }
        next_page = None
        if self.shop == 'lamoda':
            cur_page = int(response.css(stats['cur_page']).get())
            total_pages = int(response.css(stats['total_pages']).get())
            if cur_page < total_pages:
                url = response.css(stats['brand_url']).get()
                next_page = f"{url}?page={cur_page + 1}"
        else:
            url = response.css(stats['next_page']).get()
            next_page = f"{stats['base_page']}{url}"
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)
