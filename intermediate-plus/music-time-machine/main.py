import requests
from bs4 import BeautifulSoup

# period = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
period = "1998-08-25"
URL = f"https://www.billboard.com/charts/hot-100/{period}"

response = requests.get(URL)
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")

# Additional line because the TOP 1 song had a different class than the other songs
top_song = soup.find(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                       "u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 "
                                       "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 "
                                       "u-max-width-230@tablet-only u-letter-spacing-0028@tablet")


songs = soup.findAll(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                       "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                       "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 "
                                       "u-max-width-230@tablet-only")

song_names = [song.getText().strip() for song in songs]
song_names.insert(0, top_song.getText().strip())

print(song_names)