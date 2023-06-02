import scrapy


class TrendRepoFilesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://github.com/trending/rust?since=monthly",
    ]

    def parse(self, response):
        for quote in response.css(".Box-row"):
            repo_page = quote.css('h2 a::attr("href")').get()
            if repo_page is not None:
                repo_page = response.urljoin(repo_page)
                yield scrapy.Request(repo_page, callback=self.parse_repo)

    def parse_repo(self, response):
        for quote in response.css(".Box-row"):
            filename  = quote.css('[role="rowheader"] a::text').get()
            yield {
                "filename": filename
            }