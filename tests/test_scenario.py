""" test scenario module """
import os
import PIL
import pytest
from linga.scenario import run_transcribe
from linga.scenario import create_comics, Levels
from linga.scenario import create_scenario, create_image


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


def test_run_scenario():
    """tests basic script"""
    path = os.getcwd() + "/tests/resources/sample-4.mp3"
    expected = (
        " or was of heaven mine. Thus was then she."
        + " What as-be said Sarah, as to Lady for better, very stob."
    )
    assert run_transcribe(path) == expected
