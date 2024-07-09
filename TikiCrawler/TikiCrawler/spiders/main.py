import scrapy
from selenium import webdriver
from scrapy.utils.project import get_project_settings
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from TikiCrawler.items import TikiItem

URLs = ['https://tiki.vn/nha-sach-tiki/c8322',
        'https://tiki.vn/nha-cua-doi-song/c1883',
        'https://tiki.vn/dien-thoai-may-tinh-bang/c1789',
        'https://tiki.vn/do-choi-me-be/c2549',
        'https://tiki.vn/thiet-bi-kts-phu-kien-so/c1815',
        'https://tiki.vn/dien-gia-dung/c1882',
        'https://tiki.vn/lam-dep-suc-khoe/c1520',
        'https://tiki.vn/o-to-xe-may-xe-dap/c8594',
        'https://tiki.vn/thoi-trang-nu/c931',
        'https://tiki.vn/bach-hoa-online/c4384',
        'https://tiki.vn/the-thao-da-ngoai/c1975',
        'https://tiki.vn/thoi-trang-nam/c915',
        'https://tiki.vn/cross-border-hang-quoc-te/c17166',
        'https://tiki.vn/laptop-may-vi-tinh-linh-kien/c1846',
        'https://tiki.vn/giay-dep-nam/c1686',
        'https://tiki.vn/dien-tu-dien-lanh/c4221',
        'https://tiki.vn/giay-dep-nu/c1703',
        'https://tiki.vn/may-anh/c1801',
        'https://tiki.vn/phu-kien-thoi-trang/c27498',
        'https://tiki.vn/ngon/c44792',
        'https://tiki.vn/dong-ho-va-trang-suc/c8371',
        'https://tiki.vn/balo-va-vali/c6000',
        'https://tiki.vn/voucher-dich-vu/c11312',
        'https://tiki.vn/tui-vi-nu/c976',
        'https://tiki.vn/tui-thoi-trang-nam/c27616',
        'https://tiki.vn/cham-soc-nha-cua/c15078']

class MainSpider(scrapy.Spider):
    name = "main"

    def start_requests(self):
        settings = get_project_settings()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        service = Service(executable_path=settings.get('CHROME_DRIVER_PATH'))
        driver = webdriver.Chrome(options=options, service=service)
        for url in URLs:
            driver.get(url)
            time.sleep(3)
            while True:
                try:
                    next = driver.find_element(By.CSS_SELECTOR, '.styles__Button-sc-143954l-1').click()
                    time.sleep(2)
                except:
                    break
            link_elements = driver.find_elements(By.CSS_SELECTOR, 'a.product-item')
            for link in link_elements:
                href = link.get_attribute("href")
                yield scrapy.Request(href)


    def parse(self, response):
        main = response.css('main')
        tiki_items = TikiItem()
        tiki_items['name'] = main.css('h1::text').get()
        tiki_items['brand'] = main.css('span.brand-and-author h6 a::text').get()
        tiki_items['category'] = main.css('a[class="breadcrumb-item"][data-view-index="1"] span::text').get()
        tiki_items['primary_category'] = main.css('a[class="breadcrumb-item"][data-view-index="2"] span::text').get()
        tiki_items['total_rating'] = main.css('a.number[data-view-id="pdp_main_view_review"]::text').get()
        tiki_items['average_rating'] = main.css('div[class="styles__StyledReview-sc-1onuk2l-1 dRFsZg"] div::text').get()
        tiki_items['sold'] = main.css('div[data-view-id="pdp_quantity_sold"][class="styles__StyledQuantitySold-sc-1onuk2l-3 eWJdKv"]::text').get()
        tiki_items['price'] = main.css('div.product-price__current-price::text').get()
        tiki_items['url'] = response.url
        yield tiki_items
