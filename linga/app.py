""" flask app """
from flask import Flask
from scenario import run_transcribe


app = Flask(__name__, "/static")


@app.route("/")
def get_canvas():
    """return static content"""
    return app.send_static_file("index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe():
    """return static content"""
    try:
        res = run_transcribe('')
        return res, 500
    except Exception as e:
        return "Transcription failed", 500
