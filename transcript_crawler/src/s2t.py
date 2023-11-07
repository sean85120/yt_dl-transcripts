import os

import openai
import whisper
from dotenv import load_dotenv

load_dotenv()
# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")
audio_dir = "../audios/"


def speech_to_text(audio):
    model = whisper.load_model("base")
    result = model.transcribe(audio)

    # Print the transcribed text
    print(result)


def audio_to_text(video_file):
    audio_path = audio_dir + video_file
    with open(audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            file=audio_file,
            model="whisper-1",
            speaker_labels=True,
            language="zh",
        )
    video_title = video_file.split(".")[0]
    with open("../transcripts/" + video_title + ".txt", mode="a") as file:
        file.write("\n")
        file.write(transcript["text"])


if __name__ == "__main__":
    # Specify the audio you want to transcribe
    audio = input("Enter the audio file path: ")
    audio_to_text(audio)
