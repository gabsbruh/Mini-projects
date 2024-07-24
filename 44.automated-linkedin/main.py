import time
from os import environ
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

url = r"https://www.linkedin.com/jobs/search/?currentJobId=3981805466&f_AL=true&f_E=1%2C2&geoId=103263110&keywords=Python%20Developer&location=Krak%C3%B3w%2C%20Woj.%20Ma%C5%82opolskie%2C%20Polska&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"


def main():
    
    def abort_filling_form():
        # if filling form demanded, exit
        exit_ = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        exit_.click()
        time.sleep(2)
        
        # abort and delete this application
        discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
        discard_button.click()           
    
    # load environmental variables
    load_dotenv()
    
    # environmental variables
    user_login = environ["login"]
    user_password = environ["password"]
    user_phone_number = environ["phone_number"]
    
    # keep site open
    driver_options = webdriver.ChromeOptions()
    driver_options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome()
    driver.get(url=url)
    
    # click for sign in
    sign_in = driver.find_element(By.XPATH, value="/html/body/div[3]/header/nav/div/a[2]")
    sign_in.click()
    del sign_in
    time.sleep(2)
    
    # sign in to account
    login = driver.find_element(By.ID, value="username")
    login.send_keys(user_login)

    password = driver.find_element(By.ID, value="password")
    password.send_keys(user_password)
    
    log_in = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
    log_in.click()
    time.sleep(2)
    del login, password, log_in

    # get all offers
    offers = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

    # apply for offers which has quick apply w/o filling forms
    for offer in offers:
        offer.click()
        try:
            apply = driver.find_element(By.CSS_SELECTOR, value='.jobs-search__job-details--wrapper button.artdeco-button--primary')
            apply.click()
        except NoSuchElementException:
            # filters included only fast application. In case there's no button, job had been applied before
            continue
        time.sleep(3)
        del apply

        try:
            # add phone number
            number = driver.find_element(By.CLASS_NAME, value="artdeco-text-input--input")
            if number.text == "":
                number.send_keys(user_phone_number)
            time.sleep(2)
            # forward
            forward = driver.find_element(By.CSS_SELECTOR, value="form footer button")
            forward.click()
            time.sleep(2)
            del number, forward
            # skip updating resume - next forward
            forward = driver.find_element(By.CSS_SELECTOR, value="footer button.artdeco-button--primary")
            if forward.get_attribute("data-control-name") == "continue_unify":
                abort_filling_form()
            else:
                forward.click()
            time.sleep(2)
            del forward
            # send application
            send = driver.find_element(By.CSS_SELECTOR, value="footer button.artdeco-button--primary")
            if send.get_attribute("data-control-name") == "continue_unify":
                abort_filling_form()
            else:
                send.click()
            time.sleep(2)
            del send
            
        except NoSuchElementException:
            abort_filling_form()


if __name__ == "__main__":
    main()
