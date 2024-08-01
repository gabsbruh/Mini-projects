import time
import constants as c
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from functools import wraps
from property_data import Property_

# time sleep decorator
def delay(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Waiting for {seconds} seconds before calling {func.__name__}")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

class FillForm:
    # take property and fill to google form for save its data in sheet
    def __init__(self, form_url=c.GOOGLE_FORM_LINK):
        self.form_url = form_url
        
        # # add webdriver options
        # self.driver_options = webdriver.ChromeOptions()
        # self.driver_options.add_experimental_option("detach", True)
        
        # initialize webdriver
        self.driver = webdriver.Chrome()
        self.driver.get(url=self.form_url)
    
    @delay(0.1)
    def fill_out_form(self, property_: Property_):
        
        # get essential elements for mutiple use
        input_elements = self.driver.find_elements(By.CLASS_NAME, value="KHxj8b")
        send_button = self.driver.find_element(By.CLASS_NAME, value="VkkpIf")
        input_elements[0].send_keys(property_.location)
        input_elements[1].send_keys(property_.price)
        input_elements[2].send_keys(property_.size)
        input_elements[3].send_keys(property_.link)
        send_button.click()
        self.driver.back()

