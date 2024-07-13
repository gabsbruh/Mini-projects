import datetime as dt
import constants as c
from billboard_scrap import BillboardScrap
from spotify_manager import SpotifyManager

def main():
    while True:
        try:
            date = input("\nWhich year would you like to travel to? Specify the date in format 'YYYY-MM-DD'")
            date_obj = dt.datetime.strptime(date, r"%Y-%m-%d")
            if date_obj < c.FIRST_BILLBOARD_CHART:
                # check if date isn't older than first listing on the billboard
                print("The date You entered is too far in the past.\nEarliest possible is ", date_obj)
            else:
                break
        except ValueError:
            print("Wrong input. Try again")
        
        

if __name__ == "__main__":
    main()
