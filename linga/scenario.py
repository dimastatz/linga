""" generates comics scenarious """
from enum import Enum


class Levels(Enum):
    """Scenarios dificulty levels"""

    BEGINNER = 1
    MEDIUM = 2
    ADVANCED = 3


def create_comics(topic: str, level: Levels, pages: int) -> str:
    """creates comics with"""
    return f"{topic} {level} {pages}"
