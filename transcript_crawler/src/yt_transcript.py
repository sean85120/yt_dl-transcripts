from youtube_transcript_api import YouTubeTranscriptApi

video_id = "yc2nLEA7ZT0"


def get_video_script(video_id, video_title=video_id):
    transcript = YouTubeTranscriptApi.get_transcript(
        video_id=video_id, preserve_formatting=True, languages=["zh-TW"]
    )
    with open(f"../transcripts/{video_title}.txt", "w") as f:
        for line in transcript:
            f.write(line["text"] + "\n")


def is_caption_avaliable(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        return transcript_list.find_transcript(["zh-TW"]) is not None

    except:
        transcript_list = None
        # print('transcript:',transcript_list)
        return transcript_list


if __name__ == "__main__":
    get_video_script(video_id)
