""" generates comics scenarious """
from enum import Enum
from PIL import Image
import requests


class Levels(Enum):
    """Scenarios dificulty levels"""

    BEGINNER = 1
    MEDIUM = 2
    ADVANCED = 3


def create_image(description: str, bearer: str) -> Image:
    """create image by description"""
    url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": f"Bearer {bearer}"}
    response = requests.post(
        url, headers=headers, json={"inputs": description}, timeout=120
    )
    return response.content


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
