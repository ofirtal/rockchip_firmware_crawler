from connect_to_page import ConnectToPage
from crawler_frame import CrawlerMainFrame
from url_gen import UrlGen
import argparse


class CrawlerMain:
    """
    Iterates over pages and get from each page all links to firmware file and metadata pages
    """
    def __init__(self, base_page_link):
        """
        :param base_page_link: a root web page for the crawler
        """

        self.count_page = 0
        self.count_firmware_links = 0
        self.base_page = base_page_link
        self.base_page_downloads_link = self.get_download_link()
        self.url_generator = UrlGen(self.base_page)
        self.page = self.base_page_downloads_link

    def go_over_pages(self):

        while self.page is not None:
            self.count_page += 1
            print('Page:', self.count_page, 'page_link: ', self.page)
            print('Total links so far: ', self.count_firmware_links)

            links_of_page = self.url_generator.all_links_in_page(self.page)

            for link in links_of_page:
                self.count_page += 1
                print(link)
                CrawlerMainFrame(self.base_page, link, self.page).executes_scraping()
            self.page = self.url_generator.next_page(self.page)

    def get_download_link(self):
        soup = ConnectToPage(self.base_page).get_soup()
        link = soup.find('a', {'title': "Download"})
        href_link = link.get('href')
        return f'{self.base_page}/{href_link}'


if __name__ == "__main__":
    #
    # parser = argparse.ArgumentParser()
    # parser.add_argument('website', help='Enter website url', type=str)
    # args = parser.parse_args()
    #
    # CrawlerMain(args.website)
    CrawlerMain('https://www.rockchipfirmware.com').go_over_pages()

# crawler_main.py https://www.rockchipfirmware.com