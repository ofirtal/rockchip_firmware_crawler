import firmware_download
from MongoAtlasConnect import MongoAtlasConnect
from connect_to_page import ConnectToPage
from firmware_download import DownloadFirmware
from get_metadata import GetMetaData
from new_dir import NewDirectory


class CrawlerMainFrame:
    def __init__(self, base, url, page):
        """
        :param base: URL that initialized the crawl
        :param page: page url containing al inside page urls
        :param url: inside page url containing the firmware file and raw data

        """
        self.page = page
        self.base_url = base
        self.target_url = url
        self.path = NewDirectory('firmware_files').new_dir_path()
        print('created new dir')

        self.executes_scraping()

    def create_soup(self):
        """creates inside page soup"""
        soup = ConnectToPage(self.target_url)
        print('inside page soup created')
        return soup

    def executes_scraping(self):
        """in each inside page it extracts firmware file link, download file,
         extracts page metadata as dict and pushes the metadata into mongodb"""
        inside_page_soup = self.create_soup().soup

        file_name = DownloadFirmware(inside_page_soup, self.path).download_zip()
        print('{} downloaded'.format(file_name))

        metadata_dict = GetMetaData(inside_page_soup, file_name, self.page).get_metadata()
        print('metadata ok')

        MongoAtlasConnect(metadata_dict, 'arc_test_db', 'firmware files')
        "pushed to Mongo"




