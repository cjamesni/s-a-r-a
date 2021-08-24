import aiohttp
import asyncio
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

start_time = time.time()
scope = "user-top-read"
ranges = ['short_term', 'medium_term', 'long_term']
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config("client_id"),
                                               client_secret=config("client_secret"),
                                               redirect_uri=config("redirect_uri"),
                                               scope=scope))


async def main():
    async with aiohttp.ClientSession() as session:
        for sp_range in ranges:
            print("range:", sp_range)
            results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
            async with session.get(results) as resp:
                for i, item in enumerate(results['items']):
                    print(i, item['name'], '//', item['artists'][0]['name'])
                print()


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
