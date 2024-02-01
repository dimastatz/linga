""" perform fast transcription """
import numpy as np
from faster_whisper import WhisperModel


Model = WhisperModel("large-v3")


def transcribe(buffer: np.ndarray) -> str:
    """perform in memory transcription"""
    segments, _ = Model.transcribe(buffer, language="en", beam_size=5)
    return str.join(" ", [x.text for x in segments])
