from connect_to_page import ConnectToPage


class UrlGen:
    def __init__(self, base_url):
        self.base_url = base_url

    def all_links_in_page(self, page_url):
        soup = ConnectToPage(page_url).soup
        links = soup.find_all('td', {'class': 'views-field views-field-title'})
        for link in links:
            link_a_tags = link.find('a')
            link_href = link_a_tags.get('href').replace('\\', '/')
            yield self.full_link(link_href)

    def next_page(self, page_url):
        soup = ConnectToPage(page_url).soup
        next_link = soup.find('a', {'title': 'Go to next page'})

        if next_link is not None:
            next_full_link = self.full_link(next_link.get('href'))
            print(next_full_link)
            return next_full_link

    def full_link(self, link):
        return '{}/{}'.format(self.base_url, link)


