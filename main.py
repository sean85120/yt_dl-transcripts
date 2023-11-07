from transcript_crawler.src.id_crawler import get_video_ids_from_playlist
from transcript_crawler.src.split_and_transcribe import audio_to_text
from transcript_crawler.src.yt_downloader import download_audio
from transcript_crawler.src.yt_transcript import get_video_script, is_caption_avaliable


def main(playlist_id):
    video_list = get_video_ids_from_playlist(playlist_id)
    video_list.pop(0)
    video_list.pop(0)
    print("video_list:", video_list)

    for index, video_id in enumerate(video_list):
        print(f"processing video {index + 1}")
        caption_is_avaliable = is_caption_avaliable(video_id)

        video_url = f"https://youtu.be/{video_id}"
        try:
            audio_name = download_audio(video_url)
        except:
            print("Failed to download video")
            continue

        print(f"finished downloading {audio_name}")

        if caption_is_avaliable:
            print(True)
            get_video_script(video_id, audio_name)
        else:
            print(None)

            audio_to_text(f"{audio_name}.wav")

        print(f"finished processing {audio_name}")


if __name__ == "__main__":
    playlist_id = "PLE89H9C5A6WMP2v9uP4K0LhJ-hb2pZxjU"
    main(playlist_id)
