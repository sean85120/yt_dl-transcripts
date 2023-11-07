import os
import subprocess

import openai
from dotenv import load_dotenv
from pydub import AudioSegment

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")


audio_dir = "../audios/"
segment_dir = "../audios/segments/"


def audio_to_text(video_title):
    audio_path = audio_dir + video_title
    file_format = video_title.split(".")[1]
    wav_file = AudioSegment.from_file(file=audio_path, format=file_format)

    segments = int(wav_file.duration_seconds // (60 * 2)) + 1
    if segments < 2:
        transcript = openai.Audio.transcribe(
            file=audio_path,
            model="whisper-1",
            speaker_labels=True,
            language="zh",
        )
        with open("./transcripts/" + video_title + ".txt", mode="a") as file:
            file.write("\n")
            file.write(transcript["text"])
    else:
        for i in range(segments):
            start = i * 60 * 2 * 1000
            end = (i + 1) * 60 * 2 * 1000
            segment = wav_file[start:end] if i != segments - 1 else wav_file[start:]
            segment_file = segment.export(
                audio_dir
                + "segments/"
                + video_title
                + str(i + 1)
                + "_"
                + str(segments)
                + ".wav",
                format="wav",
            )

            print(segment_file.name)

            segment_audio = open(segment_file.name, "rb")
            transcript = openai.Audio.transcribe(
                file=segment_audio,
                model="whisper-1",
                speaker_labels=True,
                language="zh",
            )

            with open("./transcripts/" + video_title + ".txt", mode="a") as file:
                file.write("\n")
                file.write(transcript["text"])

            subprocess.run(["rm", segment_file.name])


def segment_wav_file(video_file):
    audio_path = audio_dir + video_file

    wav_file = AudioSegment.from_file(file=audio_path, format="wav")

    segments = int(wav_file.duration_seconds // 15) + 1
    if segments < 2:
        pass
    else:
        for i in range(segments):
            start = i * 15 * 1000
            end = (i + 1) * 15 * 1000
            segment = wav_file[start:end] if i != segments - 1 else wav_file[start:]
            segment_file = segment.export(
                audio_dir
                + "/segments/"
                + video_file.split(".")[0]
                + str(i + 1)
                + "_"
                + str(segments)
                + ".wav",
                format="wav",
            )

            print(segment_file.name)


def segment_to_2mins(file_path):
    # segment_dir = "../voice_changer/raw_audios/"
    filename = file_path.split("/")[-1].split(".")[0]

    wav_file = AudioSegment.from_file(file=file_path, format="wav")

    segments = int(wav_file.duration_seconds // (60)) + 1
    if segments < 4:
        pass
    else:
        for i in range(segments):
            start = i * 60 * 2 * 1000
            end = (i + 1) * 60 * 2 * 1000
            segment = wav_file[start:end] if i != segments - 1 else wav_file[start:]
            if i == 1:
                segment_file = segment.export(
                    segment_dir + filename + str(i + 1) + "_" + str(segments) + ".wav",
                    format="wav",
                )

    print("segment_file:", segment_file.name)
    return segment_file.name


if __name__ == "__main__":
    # file_path = input("please enter the filename in /audios: ")
    # audio_to_text(file_path)
    video_file = input("please enter the filename in /audios ")
    segment_wav_file(video_file)
