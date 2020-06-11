import requests
import zipfile
import io
import urllib.parse


class DownloadFirmware:
    """
    Checks if a page has a firmware file in it,
    then download it into a new directory that can be found in the "firmware_files" directory in the project
    """

    def __init__(self, soup, target_path):
        """

        :param soup: the soup of the target page
        :param target_path: path to "firmware_files" directory
        """
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
            file_name = urllib.parse.unquote(zip_url).split('/')[-1].replace('.zip', '')
            # firmware files are bytes-like objects, there for we need to use the io.BytesIO to interact with it.
            # mode parameter should be 'r' to read an existing file.
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(f'{self.path}/{file_name}')

        except requests.exceptions.MissingSchema:
            print('no zip file')

        file_name_to_mongo = self.soup.title.text

        return file_name_to_mongo

