import scrapy

class VneSpiderSpider(scrapy.Spider):
    name = "vne_spider"
    allowed_domains = ['vnexpress.net']
    start_urls = ["https://vnexpress.net/giai-tri",
                  "https://vnexpress.net/the-thao",
                  "https://vnexpress.net/phap-luat",
                  "https://vnexpress.net/giao-duc",
                  "https://vnexpress.net/suc-khoe",
                  "https://vnexpress.net/doi-song",
                  "https://vnexpress.net/du-lich",
                  "https://vnexpress.net/oto-xe-may"  
                  ]


    # Hàm này sẽ được gọi để lấy các liên kết và tiêu đề của các bài báo từ trang web
    def parse(self, response):
        for article in response.css(".title-news > a"):
            #phương thức follow() để tiếp tục lấy dữ liệu từ trang kế tiếp.
            yield response.follow(article, self.parse_article)

        next_page = response.css("a.next-page::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            

    def parse_article(self, response):

        title = response.css("h1::text").get()

        #dung 'response' de lay phan tu HTML cua content
        image_link = response.css("meta[property='og:image']::attr(content)").get()

        #dung 'response' de lay phan tu HTML cua content
        content = response.css(".fck_detail p::text").getall()

        # dung join de chuyen content ve thanh dang chuoi 
        content = "".join(content)
        yield {
            "title": title,
            "image_link": image_link,
            "content": content
        }
                
#scrapy crawl vne_spider
