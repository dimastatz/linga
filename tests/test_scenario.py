""" test scenario module """
from linga.scenario import create_senario
from linga.scenario import create_comics, Levels


def test_create_comics():
    """tests basic comics"""
    res = create_comics("history", Levels.BEGINNER, 7)
    assert res == "history Levels.BEGINNER 7"


def test_create_scenario():
    """tests basic script"""
    scenario = create_senario("history", Levels.BEGINNER, 7)
    assert not scenario
