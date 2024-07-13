from bs4 import BeautifulSoup
import constants as c
import requests

class BillboardScrap:
    def __init__(self, date: str):
        self.full_link = c.LINK+date
        self.html_content = self._get_html_content()
        
    def _get_html_content(self):
        response = requests.get(self.full_link)
        if response.status_code != 200:
            print("Something's wrong with link")
        else:
            return response.text
    
    def scrap_web(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        titles = soup.select("li ul li h3")
        authors = soup.select("li ul li span")
            
        songs_authors = [] # tuples containing song name and its author
        for title, author in zip(titles, authors):
            songs_authors.append((title.getText().strip(), author.getText().strip()))
        print(songs_authors)

b = BillboardScrap("1958-08-04")
b.scrap_web()
