""" test scenario module """
import io
from PIL import Image
from linga.scenario import create_comics, Levels
from linga.scenario import create_scenario, create_image


def test_create_image():
    """test hugging face image generation"""
    image_bytes = create_image("create image of spaceship landing unknown planet", "")
    image = Image.open(io.BytesIO(image_bytes))
    assert image


def test_create_comics():
    """tests basic comics"""
    res = create_comics("history", Levels.BEGINNER, 7)
    assert res == "history Levels.BEGINNER 7"


def test_create_scenario():
    """tests basic script"""
    scenario = create_scenario("history", Levels.BEGINNER, 7)
    assert not scenario
