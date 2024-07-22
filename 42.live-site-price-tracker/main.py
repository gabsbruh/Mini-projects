import requests
from os import environ
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from notification_manager import NotificationManager
from trick_live_site import HeaderSwitch
from my_header import full_header


# object for price track (PS5)
URL = "https://www.amazon.pl/dp/B0CQMPN7DY/ref=sr_1_10?sr=8-10"
# satisfying price for this
satisfying_price = 2300.00

def main():
    load_dotenv()
    
    # provide mutable header to prevent treating request like a bot & omit CAPTCHA
    header_switch = HeaderSwitch(full_header)
    header = header_switch.change_header()

    response = requests.get(url=URL, headers=header)
    soup = BeautifulSoup(response.content, "html.parser")
    price_raw = soup.find(class_="a-offscreen")
    product_title_raw = soup.find(class_="product-title-word-break")
    
    try:
        price = price_raw.getText()
        price = float(price.replace("\xa0", '').replace('zł', '').replace(',', '.'))
        product = product_title_raw.getText().strip().replace('ł', 'l')
        print(product)
        print(price)
        
    except AttributeError:
        print("CAPTCHA :((\n")
        print("Complete captcha manually here to realize further requests: https://www.amazon.pl/dp/B0CQMPN7DY/ref=sr_1_10?sr=8-10")
    
    else:
        
        if price < satisfying_price:
            notify = NotificationManager(object_name=product,
                                        price=price,
                                        email_receiver=environ["email_receiver"])
            notify.send_email()
        

if __name__ == "__main__":
    main()