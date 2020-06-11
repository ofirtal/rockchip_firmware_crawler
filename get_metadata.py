from bs4 import BeautifulSoup


class GetMetaData:
    """
    get the metadata from page. the program will get metadata even if there is no firmware file to download
    """
    def __init__(self, soup: BeautifulSoup, file_name, page):
        self.page = page
        self.soup = soup
        self.file_name = file_name

    def get_metadata(self):
        metadata_dict = {'file_name': self.file_name}

        title = self.soup.find('div', {'class': 'field field-name-title field-type-ds field-label-hidden'})
        submitted_date = self.soup.find('div', {'class': 'field field-name-submitted-by field-type-ds field-label-hidden'})

        metadata_dict['Title'] = title.text
        metadata_dict['submitted_date'] = submitted_date.text
        metadata_dict['parent_page'] = self.page

        labels = self.soup.find_all('div', {'class': "field-label"})

        for label in labels:
            link = label.next_sibling.find('a')
            clean_label = self.clean_data(label.text)
            clean_value = self.clean_data(label.next_sibling()[0].text)

            metadata_dict[clean_label] = clean_value
            if link is not None:
                metadata_dict[clean_label + '_link'] = link.get('href')

        return {'file name': str(self.file_name), 'metadata': metadata_dict}

    @staticmethod
    def clean_data(data):
        return str(data).strip().replace(':', '').replace('?', '').replace('\n', '').replace('"','')
