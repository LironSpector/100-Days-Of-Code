import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from pprint import pprint


# CLIENT_ID = "57005cfcec6e4f019c874ef6e58029a4"
# CLIENT_SECRET = "194fc3dcb0404c488f922be361b47998"
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = "http://example.com"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")

all_songs = soup.select(selector="li ul li #title-of-a-story")
songs_names = [song.getText().strip() for song in all_songs]


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               cache_path=".cache.txt"))

user_id = sp.current_user()["id"]

songs_uris = []
year = date.split("-")[0]

for song in songs_names:
    try:
        uri = sp.search(q=f"track: {song} year: {year}", type="track")["tracks"]["items"][0]["album"]["artists"][0]["uri"]
        # uri = sp.search(q=f"track: {song} year: {year}", limit=1, type="artist")
        print(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
    else:
        songs_uris.append(uri)
        break


print(songs_uris)
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)

