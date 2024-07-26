from dotenv import load_dotenv
from os import environ

load_dotenv()

# minimum required speed from internet provider
MIN_UPLOAD = 10
MIN_DOWNLOAD = 150
SPEEDTEST_URL = "https://www.speedtest.net"

# credentials to X log in
X_EMAIL = environ['email']
X_PASSWORD = environ['password']
X_HOME_URL = "https://x.com/home"
