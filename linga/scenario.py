""" generates comics scenarious """
from enum import Enum


class Levels(Enum):
    """Scenarios dificulty levels"""

    BEGINNER = 1
    MEDIUM = 2
    ADVANCED = 3


def create_senario(topic: str, level: Levels, pages: int) -> list:
    """creates scenario by using chat_gpt and returns list of pages"""
    prompt = f"{topic} {level} {pages}"
    assert prompt
    return []


def create_comics(topic: str, level: Levels, pages: int) -> list:
    """creates comics with"""
    pages_list = create_senario(topic, level, pages)
    assert len(pages_list) == 0
    return f"{topic} {level} {pages}"
