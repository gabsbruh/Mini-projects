import smtplib
from user import User
from data_manager import DataManager
import constants as c

class NotificationManager:
    def __init__(self, users_list, info_about_flights):
        self.users = users_list
        self.info_about_flights = info_about_flights['prices']
    
    def send_emails(self):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connect:
            connect.starttls() # secure the connection
            # log in to the account.
            my_email = c.MY_EMAIL
            connect.login(user=my_email, password=c.PASS) 
            for info in self.users: # send email for each person in flight club
                formula = self._create_message(info.name, info.surname)
                connect.sendmail(from_addr=my_email, to_addrs=info.email,
                                msg=f"Subject:Flight Club - new offers!\n\n{formula}")

    def _create_message(self, name, surname):
        offer = []
        for city in self.info_about_flights:
            offer.append(f"Trip to {city['city']} - now only for {city['cheapest']}PLN! ({city['departureDate']} to {city['arrivalDate']}, by {city['departureCarrier']})")
        return '\n'.join(offer)
