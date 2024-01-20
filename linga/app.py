""" flask app """
import tempfile, os
from flask import Flask, request
from linga.scenario import run_transcribe


app = Flask(__name__, "/static")


@app.route("/")
def get_canvas():
    """return static content"""
    return app.send_static_file("index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe():
    """return static content"""
    try:
        f = request.files['file']
        fd, path = tempfile.mkstemp()
        os.write(fd, f.stream)
        os.close(fd)

        return (f.filename, path), 200
    except Exception as e:
        return f"Transcription failed {e}", 500
