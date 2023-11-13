""" test scenario module """
from linga.scenario import create_comics, Levels


def test_index():
    """tests basic flow"""
    res = create_comics("history", Levels.BEGINNER, 7)
    assert res == "history Levels.BEGINNER 7"
