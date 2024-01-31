""" perform fast transcription """
from faster_whisper import WhisperModel


Model = WhisperModel("large-v3", device="cuda", compute_type="float16")


def transcribe(buffer: np.ndarray) -> str:
    """perform in memory transcription"""
    segments, info = Model.transcribe(buffer, beam_size=5)
    return segments