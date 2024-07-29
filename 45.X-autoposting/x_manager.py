import time
import constants as c
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class XManager:
    # move trough X website by this app
    def __init__(self, upload_speed, download_speed, email=c.X_EMAIL, 
                 username=c.X_USERNAME, password=c.X_PASSWORD):
        
        self.url = c.X_HOME_URL
        self.email = email
        self.username = username
        self.password = password
        
        # info about internet speed
        self.download_speed = download_speed
        self.upload_speed = upload_speed
        
        # initialize webdriver
        self.driver = webdriver.Chrome()
        self.driver.get(url=self.url)
        
        # add webdriver options
        self.driver_options = webdriver.ChromeOptions()
        self.driver_options.add_experimental_option("detach", True)
        
        # log in to X platform
        self._log_in()
        
    def _choose_content_of_complaint(self, content=c.X_POST_CONTENTS):
        if isinstance(content, list):
            post_content = random.choice(content)
            post_content = post_content.replace('[PROVIDER]', c.INTERNET_PROVIDER_ACCOUNT)
            post_content = post_content.replace('[DOWNLOAD_FLOAT]', str(self.download_speed))
            post_content = post_content.replace('[UPLOAD_FLOAT]', str(self.upload_speed))
        else:
            post_content = content
        return post_content
    
    def post_complaint(self):
        time.sleep(7)
        content = self._choose_content_of_complaint()
        input_for_post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        input_for_post.send_keys(content)
        time.sleep(10)
        # post_button = self.driver.find_element(By.CLASS_NAME, value='r-1cwvpvk')
        # post_button.click()        
        
    def _log_in(self):
        time.sleep(4)
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", login_button)
        
        time.sleep(2)
        input_email = self.driver.find_element(By.CSS_SELECTOR, value="input")
        input_email.send_keys(self.email)
        forward = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        forward.click()
        
        time.sleep(2)
        input_username = self.driver.find_element(By.CSS_SELECTOR, value='input')
        input_username.send_keys(self.username)
        time.sleep(1)
        forward_2 = self.driver.find_element(By.CLASS_NAME, value='r-64el8z')
        forward_2.click()        
        
        time.sleep(2)
        input_password = self.driver.find_element(By.CLASS_NAME, value='r-homxoj')
        input_password.send_keys(self.password)
        time.sleep(1)
        go_in = self.driver.find_element(By.CLASS_NAME, value='r-64el8z')
        go_in.click()
    