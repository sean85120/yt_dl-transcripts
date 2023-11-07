import subprocess

import moviepy.editor as mp
from pytube import YouTube

# video_url = "https://youtu.be/5i86KxtLk4E"

# VIDEO_SAVE_DIRECTORY = "./videos"
AUDIO_SAVE_DIRECTORY = "../audios"


def download_audio(video_url):
    yt = YouTube(video_url)
    yt_audio = yt.streams.get_lowest_resolution()
    yt_title = yt.title

    try:
        output_audio = yt_audio.download(AUDIO_SAVE_DIRECTORY)
        clip = mp.VideoFileClip(output_audio)

        clip.audio.write_audiofile(AUDIO_SAVE_DIRECTORY + "/" + yt_title + ".wav")

        subprocess.run(["rm", output_audio])

    except:
        print("Failed to download video")

    print("audio was downloaded successfully")

    return yt_title


def download_video(video_url):
    yt = YouTube(video_url)
    yt_title = yt.title

    yt_downloader = (
        yt.streams.filter(progressive=True, file_extension="mp4").first().download()
    )

    print("video was downloaded successfully")

    return yt_title


if __name__ == "__main__":
    video_url = input("Enter the video url: ")
    download_video(video_url)
