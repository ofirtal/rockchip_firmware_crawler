from bs4 import BeautifulSoup
import requests

"""
connects to a page, returning its "soup" data
"""


class ConnectToPage:
    def __init__(self, target_url):
        self.url = target_url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
