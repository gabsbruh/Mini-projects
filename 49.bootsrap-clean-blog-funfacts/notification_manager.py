import smtplib
import os

class NotificationManager:
    def __init__(self, data, email_receiver):
        self.data = data
        self.receiver = email_receiver
        self._user = os.environ.get('MY_EMAIL')
        self._password = os.environ.get('EMAIL_SECRET')
    
    def send_email(self):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connect:
            connect.starttls() # secure the connection
            # log in to the account.
            formula = f"""
            Name:  {self.data['name']}
            Email: {self.data['email']}
            Phone: {self.data['phone']}
            Message:
                {self.data['message']}
            """
            
            connect.login(user=self._user, password=self._password) 
            connect.sendmail(from_addr=self._user, to_addrs=self.receiver,
                            msg=f"Subject: Blog Post email from '{self.data['name']}'\n\n{formula}")

    @property
    def password(self):
        return self._password
    
    @property
    def user(self):
        return self._user
    