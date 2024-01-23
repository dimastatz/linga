""" flask app """
import logging
import traceback
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
        logging.info(f"file path{fd}, {path}")
        f.save(path)

        text = run_transcribe(path), 200
        os.remove(path)
        return text
    except Exception as e:
        logging.error(traceback.format_exc())
        return f"Transcription failed {e}", 500
