from unittest.mock import mock_open, patch

import pytest
from src.split_and_transcribe import (
    audio_to_text,
)  # Assuming your function is in 'yourmodule.py'

# Mock the external openai library
openai_mock = pytest.importorskip("openai")


@pytest.fixture
def setup_audio_segment_mock():
    with patch("src.split_and_transcribe.AudioSegment") as mock:
        yield mock


@pytest.fixture
def setup_openai_mock():
    with patch("src.split_and_transcribe.openai.Audio.transcribe") as mock:
        mock.return_value = {"text": "transcribed text"}
        yield mock


@pytest.fixture
def setup_file_operations_mock():
    with patch("builtins.open", new_callable=mock_open) as mock:
        yield mock


@pytest.fixture
def setup_subprocess_mock():
    with patch("src.split_and_transcribe.subprocess.run") as mock:
        yield mock


def test_audio_to_text_single_segment(
    setup_audio_segment_mock, setup_openai_mock, setup_file_operations_mock
):
    audio_dir = "/fake/dir/"
    video_title = "video.mp4"

    # Assume duration_seconds is less than 2 minutes, no segmentation needed.
    setup_audio_segment_mock.from_file.return_value.duration_seconds = 60

    audio_to_text(video_title)

    # Verify that openai.Audio.transcribe was called once
    setup_openai_mock.assert_called_once()

    # Verify that the file write operations happened as expected
    setup_file_operations_mock.assert_called()
    handle = setup_file_operations_mock()
    handle.write.assert_called_with("transcribed text")


@pytest.mark.parametrize("duration_seconds", [120, 240])
def test_audio_to_text_multiple_segments(
    setup_audio_segment_mock,
    setup_openai_mock,
    setup_file_operations_mock,
    setup_subprocess_mock,
    duration_seconds,
):
    audio_dir = "/fake/dir/"
    video_title = "video.mp4"

    # Set up the mock to provide a fake duration in seconds that would lead to multiple segments
    setup_audio_segment_mock.from_file.return_value.duration_seconds = duration_seconds

    audio_to_text(video_title)

    # Verify that openai.Audio.transcribe was called the expected number of times
    expected_segments = int(duration_seconds // (60 * 2)) + 1
    assert setup_openai_mock.call_count == expected_segments

    # Verify that the file write operations happened as expected
    handle = setup_file_operations_mock()
    assert (
        handle.write.call_count == 2 * expected_segments
    )  # Once for newline, once for text per segment

    # Verify subprocess.run was called to remove the segment files
    assert setup_subprocess_mock.call_count == expected_segments
