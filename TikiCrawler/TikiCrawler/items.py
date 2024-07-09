# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class TikiItem(scrapy.Item):
    id = Field()
    name = Field()
    brand = Field()
    category = Field()
    primary_category = Field()
    total_rating = Field()
    average_rating = Field()
    sold = Field()
    price = Field()
    url = Field()




