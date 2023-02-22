import requests
import os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
                                               client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               cache_path="token.txt",
                                               show_dialog=True
                                               )
                     )

user_id = sp.current_user()["id"]

period = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# period = "1998-08-25"

URL = f"https://www.billboard.com/charts/hot-100/{period}"

response = requests.get(URL)
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")

# Additional line because the TOP 1 song had a different class than the other songs
# top_song = soup.find(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
#                                        "u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 "
#                                        "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 "
#                                        "u-max-width-230@tablet-only u-letter-spacing-0028@tablet")


songs = soup.findAll(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                       "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                       "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 "
                                       "u-max-width-230@tablet-only")

song_names = [song.getText().strip() for song in songs]
# song_names.insert(0, top_song.getText().strip())

song_uris = []
year = period.split("-")[0]
five_years_before = str(int(year)-10)

for song in song_names:
    result = sp.search(q=f"track:{song} year:{five_years_before}-{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Cannot find '{song}'.")

new_playlist = sp.user_playlist_create(user=user_id, name=f"{period} Billboard TOP 100", public=False)
playlist_id = new_playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id,
                      items=song_uris)
