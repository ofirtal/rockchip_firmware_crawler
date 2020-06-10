from connect_to_page import ConnectToPage
from crawler_frame import CrawlerMainFrame
from url_gen import UrlGen
import argparse


class Main:
    def __init__(self, base_page_link):
        self.count_page = 0
        self.count_firmware_pages = 0

        self.base_page = base_page_link
        self.base_page_downloads_link = self.get_download_link()
        self.url_generator = UrlGen(self.base_page)

        page = self.base_page_downloads_link

        while page is not None:
            self.count_page += 1
            print('Page:', self.count_page, 'page_link: ', page)
            print('Total links so far: ', self.count_firmware_pages)

            links_of_page = self.url_generator.all_links_in_page(page)

            for link in links_of_page:
                self.count_page += 1
                print(link)
                CrawlerMainFrame(self.base_page, link, page)
            page = self.url_generator.next_page(page)

    def get_download_link(self):
        soup = ConnectToPage(self.base_page).soup
        link = soup.find('a', {'title': "Download"})
        return '{}/{}'.format(self.base_page, link.get('href'))


if __name__ == "__main__":
    #
    # parser = argparse.ArgumentParser()
    # parser.add_argument('website', help='Enter website url', type=str)
    # args = parser.parse_args()
    #
    # Main(args.website)
    Main('https://www.rockchipfirmware.com')

# crawler_main.py https://www.rockchipfirmware.com