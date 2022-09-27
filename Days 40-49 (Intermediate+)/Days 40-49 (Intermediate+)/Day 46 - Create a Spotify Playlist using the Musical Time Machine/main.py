import pprint as pp
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify_redirect_uri = "h"
spotify_client_id = "f"
spotify_client_secret = "9"
date = input("Deseja as musicas de que ano? Escreva a data neste formato: AAAA-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text, "html.parser")
songs_tag = soup.find_all(name="h3", class_="a-no-trucate")
songs_list = [song.getText().replace("\n", "").replace("\t", "") for song in songs_tag]
artists_tag = soup.find_all(name="span", class_="a-no-trucate")
artists_list = [artist.getText().replace("\n", "").replace("\t", "") for artist in artists_tag]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", redirect_uri=spotify_redirect_uri, client_id=spotify_client_id, client_secret=spotify_client_secret, show_dialog=True, cache_path="token.txt"))
user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # pp.pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} essa não existe no Spotify. Pulada.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
