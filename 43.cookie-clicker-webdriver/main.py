import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

def main():
    # disable closing
    driver_options = webdriver.ChromeOptions()
    driver_options.add_experimental_option("detach", True)
    
    # create automatic driver
    driver = webdriver.Chrome()
    driver.get("https://orteil.dashnet.org/experiments/cookie/")
    cookie = driver.find_element(By.ID, value="cookie")

    baking = True
    def purchase():
        available_products = ['Time machine', 'Portal', 'Alchemy lab', 'Shipment', 'Mine', 'Factory', 'Grandma', 'Cursor']
        for product in available_products:
            try:
                store_item = driver.find_element(By.XPATH, value =f'//*[@id="buy{product}"]/b')
                price = int(store_item.text.split('-')[1].strip().replace(',', ''))
                if int(driver.find_element(By.ID, value="money").text.replace(',', '')) > price:
                    try:
                        store_item.click()
                    except (StaleElementReferenceException, NoSuchElementException):
                        pass
            except StaleElementReferenceException:
                pass
    a = 150
    five_min = time.time() + 60*5 # time for end
    while baking:
        for i in range(a):
            cookie.click()
        purchase()
        # end game after 5 minutes
        if time.time() > five_min:
            cps = driver.find_element(By.ID, value='cps').text
            print(f"Final score: {cps}")
            break
        a += 50

if __name__ == "__main__":
    main()