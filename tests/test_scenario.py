""" test scenario module """
import PIL
import pytest
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
