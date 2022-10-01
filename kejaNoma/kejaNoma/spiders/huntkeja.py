import scrapy


class HuntkejaSpider(scrapy.Spider):
    name = 'huntkeja'
    start_urls = ["https://www.buyrentkenya.com/houses-for-sale"]

    def parse(self,response):
        # get details from a div
        for post in response.css(".lg\:mt-0"):
            yield {
                "title": post.css(".capitalize .text-black ::text").extract(), # good
                "Location": post.css(".mt-1.md\:mt-0 ::text").extract(), # good
                "details":post.css("span.text-sm.mr-5 ::text").extract(),
                "Price":post.css(".text-lg .no-underline ::text").extract(), # good
                "Description":post.css(".text-black.no-underline.block ::text").extract(), # good
            }


        # next_page = response.css(".hover\:bg-gray-50 ::attr(href)").extract()
        
        # if next_page is not None:
        #    next_page_url = response.urljoin(next_page)
        #    yield scrapy.Request(next_page_url, callback=self.parse)

        for next_page in response.css(".hover\:bg-gray-50 ::attr(href)"):
            url = response.urljoin(next_page.extract())
            yield scrapy.Request(url, self.parse)
        
