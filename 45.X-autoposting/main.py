from internet_speed import InternetSpeed
from x_manager import XManager


def main():
    is_driver = InternetSpeed()
    is_driver.measure_speed()
    feedback = iss.report() # check if conditions are met
    if not feedback: # if conditions fulfilled, won't be executed
        x_driver = XManager(upload_speed=is_driver.upload, download_speed=is_driver.download)
        x_driver.post_complaint() 


if __name__ == "__main__":
    main()
