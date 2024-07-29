from dotenv import load_dotenv
from os import environ

load_dotenv()

# internet provider
INTERNET_PROVIDER_ACCOUNT = environ["provider"]

# minimum required speed from internet provider
MIN_UPLOAD = 10
MIN_DOWNLOAD = 150
SPEEDTEST_URL = "https://www.speedtest.net"

# credentials to X log in
X_EMAIL = environ['email']
X_USERNAME = environ['x_username']
X_PASSWORD = environ['password']
X_HOME_URL = "https://x.com/home"
X_POST_CONTENTS = ["Hey [PROVIDER], why is my internet speed so slow? I'm getting only [DOWNLOAD_FLOAT] Mbps download and [UPLOAD_FLOAT] Mbps upload. This is unacceptable!",
                   "[PROVIDER], I can't believe the poor service. My internet speed is stuck at [DOWNLOAD_FLOAT] Mbps for download and [UPLOAD_FLOAT] Mbps for upload. What's going on?",
                   "Seriously, [PROVIDER]? [DOWNLOAD_FLOAT] Mbps download and [UPLOAD_FLOAT] Mbps upload? I'm paying for much faster speeds than this. Fix it, please!",
                   "[PROVIDER], I've had enough of this slow internet. [DOWNLOAD_FLOAT] Mbps download and [UPLOAD_FLOAT] Mbps upload is way below what I need. Can you do something about it?",
                   "Getting only [DOWNLOAD_FLOAT] Mbps download and [UPLOAD_FLOAT] Mbps upload from [PROVIDER] is really frustrating. I'm not getting the service I'm paying for!"
                   ]
