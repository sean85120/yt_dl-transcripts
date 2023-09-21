import os

import openai
import whisper
from dotenv import load_dotenv

load_dotenv()
# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def speech_to_text(audio):
    model = whisper.load_model("base")
    result = model.transcribe(audio)

    # Print the transcribed text
    print(result)


if __name__ == "__main__":
    # Specify the audio you want to transcribe
    audio = input("Enter the audio file path: ")
    speech_to_text(audio)
