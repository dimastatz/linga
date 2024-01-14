""" flask app """
from flask import Flask

app = Flask(__name__, "/static")


@app.route("/")
def get_canvas():
    """return static content"""
    return app.send_static_file("index.html")


@app.route("/transcribe", methods = ['POST'])
def transcribe():
    """return static content"""
    return "Transcription finished", 200
