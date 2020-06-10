import requests
import zipfile
import io
import urllib.parse


class DownloadFirmware:

    def __init__(self, soup, target_path):
        self.soup = soup
        self.path = target_path

    def get_zip_link(self):
        links = self.soup.find_all('a', href=True)

        for link in links:
            if link['href'].endswith('.zip'):
                return link['href']

    def download_zip(self):
        zip_url = self.get_zip_link()

        try:
            r = requests.get(zip_url)
            # firmware files are bytes-like objects, there for we need to use the io.BytesIO to interact with it.
            # ZipFile The class for reading and writing ZIP files
            # mode parameter should be 'r' to read an existing file
            file_name = urllib.parse.unquote(zip_url).split('/')[-1].replace('.zip', '')

            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall('{}/{}'.format(self.path, file_name))

        except requests.exceptions.MissingSchema:
            print('no zip file')
            file_name = self.soup.title.text

        return file_name

