import datetime as dt
import constants as c
from billboard_scrap import BillboardScrap
from spotify_manager import SpotifyManager


def main():
    while True:
        try:
            date = input("\nWhich date would you like to travel to? Specify the date in format 'YYYY-MM-DD'\n")
            date_obj = dt.datetime.strptime(date, r"%Y-%m-%d")
            if date_obj < c.FIRST_BILLBOARD_CHART:
                # check if date isn't older than first listing on the billboard
                print("The date You entered is too far in the past.\nEarliest possible is ", date_obj)
            else:
                break
        except ValueError:
            print("Wrong input. Try again")
        
    # look for top 100 songs from specified date
    bs = BillboardScrap(date)
    songs_authors = bs.scrap_billboard_website()
    
    # spotify manager develops playlist based on scrap from billboard
    sm = SpotifyManager()
    
    # search for songs uri's
    year = date.split("-")[0]
    uri_list = []
    for song,artist in songs_authors:
        uri = sm.search_for_song(song_name=song, song_author=artist, year=year)
        if isinstance(uri, str):
            uri_list.append(uri)
    
    # create a playlist
    sm.create_playlist(date=date)
    
    # change cover
    sm.upload_playlist_cover_image("./billboard_cover.jpg")
    
    # add tracks to the playlist
    sm.add_tracks(uri_list)

    print(f"Playlist has been created. Check playlist here: ", sm.playlist_url)

if __name__ == "__main__":
    main()
