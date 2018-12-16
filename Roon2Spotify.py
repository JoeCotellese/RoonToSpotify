from envparse import env
import pprint
import sys
import urllib.parse
from openpyxl import load_workbook
import spotipy
import spotipy.util as util

env.read_envfile()
pprint.pprint (env.str)
my_client_id = env('SPOTIPY_CLIENT_ID')
my_client_secret = env('SPOTIPY_CLIENT_SECRET')

def find_spotify(artist, album_name):
    token = util.prompt_for_user_token("JoeCotellese","playlist-modify-private,user-library-modify",
        client_id=my_client_id,client_secret=my_client_secret,redirect_uri='http://localhost')

    sp = spotipy.Spotify(auth=token)
    print ("searching for {}:{}".format(artist, album_name))
    search = "artist:{0} album:{1}".format(artist, album_name)
    result = sp.search(q=search, type='album', limit=1)
    items = result['albums']['items']
    try:
        id = items[0]['id']
        sp.current_user_saved_albums_add(albums=[id,])
    except IndexError:
        print ("Error search for {} {}".format(artist, album_name))

if __name__ == "__main__":
    file = "test_file.xlsx"

    wb = load_workbook(filename = file)

    sheet = wb.active

    max_row = sheet.max_row
    max_column = sheet.max_column
    current_album = ""
    last_album = ""
    for i in range(2, max_row+1):
        current_album = sheet.cell(i, 2).value
        artist = sheet.cell(i,1).value
        if current_album != last_album:
            find_spotify(artist, current_album)
            last_album = current_album
