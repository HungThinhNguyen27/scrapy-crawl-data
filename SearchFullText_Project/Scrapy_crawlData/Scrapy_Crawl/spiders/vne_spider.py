import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class VneSpiderSpider(scrapy.Spider):
    name = "vne_spider"
    allowed_domains = ['vnexpress.net']
    start_urls = ["https://vnexpress.net/giai-tri","https://vnexpress.net/the-thao"]



    def parse(self, response):
        for article in response.css(".title-news > a"):
            yield response.follow(article, self.parse_article)

        next_page = response.css("a.next-page::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            

    def parse_article(self, response):
        title = response.css("h1::text").get()
        image_link = response.css("meta[property='og:image']::attr(content)").get()
        content = response.css(".fck_detail p::text").getall()
        content = "".join(content)
        yield {
            "title": title,
            "image_link": image_link,
            "content": content
        }
                
#scrapy crawl vne_spider
