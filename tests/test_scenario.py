""" test scenario module """
import os
import logging

import PIL
import pytest

import librosa as lr
from linga.scenario import create_comics, Levels
from linga.scenario import create_scenario, create_image
from linga.scenario import run_transcribe, run_transcribe_segment


def test_create_image():
    """test hugging face image generation"""
    with pytest.raises(PIL.UnidentifiedImageError):
        image = create_image("create image of spaceship landing unknown planet", "")
        assert image


def test_create_comics():
    """tests basic comics"""
    res = create_comics("history", Levels.BEGINNER, 7)
    assert res == "history Levels.BEGINNER 7"


def test_create_scenario():
    """tests basic script"""
    scenario = create_scenario("history", Levels.BEGINNER, 7)
    assert not scenario


def test_run_transcribe():
    """test transcribe"""
    path = os.getcwd() + "/tests/resources/sample-4.mp3"
    expected = (
        " or was of heaven mine. Thus was then she."
        + " What as-be said Sarah, as to Lady for better, very stob."
    )
    assert run_transcribe(path) == expected


def test_run_transcribe_segment():
    """test transcribe chunks"""
    path = os.getcwd() + "/tests/resources/sample-4.mp3"

    buffer, _ = lr.load(path)

    logging.info("mp3_lenght %s", len(buffer))

    transcribe = run_transcribe_segment()

    while len(buffer) > 0:
        chunk = buffer[0:50000]
        buffer = buffer[50000:]
        result = transcribe(chunk)
        logging.info(result)
        assert len(result) > 0
