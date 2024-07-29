import time
import constants as c
from selenium import webdriver
from selenium.webdriver.common.by import By

class InternetSpeed:
    # Get data about internet speed with this class
    def __init__(self):
        self.url = c.SPEEDTEST_URL
        
        # initialize webdriver
        self.driver = webdriver.Chrome()
        self.driver.get(url=self.url)
        
        # add webdriver options
        self.driver_options = webdriver.ChromeOptions()
        self.driver_options.add_experimental_option("detach", True)
        
        # upload and download speed
        self.upload = 0
        self.download = 0
        
    def measure_speed(self):
        start = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        start.click()
        time.sleep(60) # wait for test
        outcome = self.driver.find_elements(By.CLASS_NAME, value="result-data-large")
        self.download = float(outcome[0].text)
        self.upload = float(outcome[1].text)
    
    def report(self):
        flag = True
        print("*** INTERNET SPEED REPORT ***")
        print(f"\nYour download speed is {self.download} Mbps.")
        if self.is_downloading_good():
            print("\tIt meets the requirements :)")
        else:
            print("DOWNLOAD DOESN'T MEET THE REQUIREMENTS!")
            flag = False
        print(f"\nYour upload speed is {self.upload} Mbps.")
        if self.is_downloading_good():
            print("\tIt meets the requirements :)")
        else:
            print("UPLOAD DOESN'T MEET THE REQUIREMENTS!")   
            flag = False
        return flag     
        
    def is_downloading_good(self):
        if self.download < c.MIN_DOWNLOAD:
            return False
        else:
            return True
        
    def is_uploading_good(self):
        if self.upload < c.MIN_UPLOAD:
            return False
        else:
            return True
