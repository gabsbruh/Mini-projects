import time
import constants as c
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from property_data import Property_

class GetProperties:
    # get actual properties available for rent
    def __init__(self, default_url=c.DEF_URL, location=c.LOCATION, max_price=c.MAX_PRICE):
        self.url = self._create_link(default_url, location, max_price)
        
        # # add webdriver options
        # self.driver_options = webdriver.ChromeOptions()
        # self.driver_options.add_experimental_option("detach", True)
        
        # initialize webdriver
        self.driver = webdriver.Chrome()
        self.driver.get(url=self.url)
    
    def __del__(self):
        self.driver.quit()
        
    def get_all_properties(self) -> list:
        """return all list elements describing properties.
        scroll trough all pages from search by adding page param

        Returns:
            list: list of web scraps
        """
        # accept cookies
        time.sleep(3)
        try:
            accept = self.driver.find_element(By.XPATH, value='//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
            accept.click()
        except NoSuchElementException:
            pass
        
        # find number of pages
        time.sleep(1)
        page_amount = self.driver.find_element(By.XPATH, value="/html/body/main/div/div/div/article/section/div[3]/nav/ul/li[last()]/a/span")
        page_amount = int(page_amount.text)
        page_range = range(1, page_amount+1)
        
        # get raw_properties
        all_properties_raw = []
        for page in page_range:
            url_with_page = self.url+str(page)
            self.driver.get(url_with_page)
            properties_webelements = self.driver.find_elements(By.CLASS_NAME, value="lbk9u7d")
            properties_raw = [webelement.get_attribute("outerHTML") for webelement in properties_webelements] 
            all_properties_raw.extend(properties_raw)
        return all_properties_raw
    
    def get_info_about_property(self, html_property_content: str, base_url=c.BASE_URL) -> Property_:
        """Take single html scrap and return data about property

        Args:
            html_property_content (str): 

        Returns:
            Property_: info about property
        """
        soup = BeautifulSoup(html_property_content, 'html.parser')
        link = base_url + soup.find('a', class_='o13k6g1y')['href'] # link to offer
        location = soup.find('address', class_='o1tpwx4m').get_text() # location
        price = soup.find('span', class_='o1bbpdyd').get_text() # price for property
        area = soup.find_all('span', class_='ngl9ymk')[1].get_text() # size of property
        return Property_(location, price, area, link)
              
    def _create_link(self, default_url, location, max_price):
        return default_url + location + "/?price__lte=" + str(max_price) + "&page="
