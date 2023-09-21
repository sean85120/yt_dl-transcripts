from crawler import get_video_script, is_caption_avaliable
from id_crawler import get_video_ids
from speech_to_text import audio_to_text
from yt_downloader import download

playlist_id = "PLaqvZMhnsmfVoJD61mHGbW62AuyhIck6t"


def main(video_id):
    # video_list = get_video_ids(playlist_id)

    # for video_id in video_list:
    caption_is_avaliable = is_caption_avaliable(video_id)

    video_url = f"https://youtu.be/{video_id}"
    audio_name = download(video_url)

    if caption_is_avaliable:
        print(True)
        get_video_script(video_id, audio_name)
    else:
        print(None)

        audio_to_text(audio_name)


if __name__ == "__main__":
    video_id = input("Enter video id: ")
    main(video_id)
