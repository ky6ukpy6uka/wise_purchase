class Shops(object):
    config = {
        'wildberries':{
            'base_page':'https://www.wildberries.ru',
            'brandlist':'/wildberries/brandlist.aspx?letter=',
            'brand':'.i-brand-list > li',
            'brand_title':'::attr(alt)',
            'brand_link':'::attr(href)',
            'default_search':'/catalog/0/search.aspx?search=',
            'item':'.ref_goods_n_p',
            'item_price':'.lower-price::text',
            'item_brand':'strong.brand-name::text',
            'item_spec':'span.goods-name::text',
            'item_link':'::attr(href)',
            'next_page':'a.pagination-next::attr(href)'
        },
        # 'lamoda':{
        #     'base_page':'https://www.lamoda.ru',
        #     'brandlist':'/brands/',
        #     'brand':'.brands_content a',
        #     'brand_title':'::text',
        #     'brand_link':'::attr(href)',
        #     'default_search':'/catalogsearch/result/?q=',
        #     'item':'.products-list-item__link',
        #     'item_price':'.price__actual::text',
        #     'item_price_new':'.price__new::text',
        #     'item_price_act':'.price__action::text',
        #     'item_brand':'.products-list-item__brand::text',
        #     'item_spec':'.products-list-item__type::text',
        #     'item_link':'::attr(href)',
        #     'next_page':'.paginator__next::text',
        #     'cur_page':'::attr(data-page)',
        #     'total_pages':'::attr(data-pages)',
        #     'brand_url':'[property="og:url"]::attr("content")',
        #     'currency':'.price__currency::text'
        # }
    }