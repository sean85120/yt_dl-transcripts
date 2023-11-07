import os

import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

load_dotenv()


youtube_api_key = os.getenv("YOUTUBE_API_KEY")

video_id_list = []


def get_video_ids(playlist_id, page_token=""):
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={playlist_id}&key={youtube_api_key}&pageToken={page_token}"

    resp = requests.get(url)

    items = resp.json()["items"]

    for item in items:
        video_id_list.append(item["contentDetails"]["videoId"])

    if "nextPageToken" in resp.json():
        page_token = resp.json()["nextPageToken"]
        get_video_ids(playlist_id, page_token)

    return video_id_list


if __name__ == "__main__":
    playlist_id = "PLaqvZMhnsmfVoJD61mHGbW62AuyhIck6t"

    video_id_len = get_video_ids(playlist_id)
    print(len(video_id_len))
