# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TikiCrawlerPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Add item id into product and remove id from url
        value = adapter.get('url')
        if value is not None:
            adapter['id'] = value.split('spid=')[1]
            adapter['url'] = value.split('spid=')[0]
        else:
            value = None

        # Remove . from price and convert to int
        value = adapter.get('price')
        if value is not None:
            adapter['price'] = int(value.replace('.', ''))
        else:
            value = None

        # Remove () from total rating and convert it into integer
        value = adapter.get('total_rating')
        if value is not None:
            adapter['total_rating'] = int(value.replace('(', '').replace(')', ''))
        else:
            value = None

        # Convert average_rating to float
        value = adapter.get('average_rating')
        if value is not None:
            adapter['average_rating'] = float(value)
        else:
            value = None

        # Remove "Đã bán" inside sold
        value = adapter.get('sold')
        if value is not None:
            adapter['sold'] = value.split()[2]

        else:
            value = None

        return item
