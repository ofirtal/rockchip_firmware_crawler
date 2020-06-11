from bs4 import BeautifulSoup
import requests


class ConnectToPage:
    """
    connects to a page, returning its "soup" data
    """
    def __init__(self, target_url):
        self.url = target_url

    def get_soup(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
