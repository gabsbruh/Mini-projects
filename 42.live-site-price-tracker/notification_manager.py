import smtplib
import os

class NotificationManager:
    def __init__(self, object_name, price, email_receiver):
        self.object_name = object_name
        self.price = price
        self.receiver = email_receiver
        self.user = os.environ.get('MY_EMAIL')
        self.password = os.environ.get('EMAIL_SECRET')
    
    def send_email(self):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connect:
            connect.starttls() # secure the connection
            # log in to the account.
            formula = f"Price of {self.object_name} went down to {self.price}PLN!"
            
            connect.login(user=self.user, password=self.password) 
            connect.sendmail(from_addr=self.user, to_addrs=self.receiver,
                            msg=f"Subject: Discount for '{self.object_name}'!\n\n{formula}")
