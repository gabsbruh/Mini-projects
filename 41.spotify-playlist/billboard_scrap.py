from bs4 import BeautifulSoup
import constants as c

class BillboardScrap():
    def __init__(self, date: str):
        self.full_link = c.LINK+date
        
    def scrap_web(self):
        pass
