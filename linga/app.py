""" flask app """
import os
import logging
import tempfile
import traceback
from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room
from linga.scenario import run_transcribe


app = Flask(__name__, "/static")
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def get_canvas():
    """return static content"""
    return app.send_static_file("index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe():
    """return static content"""
    try:
        file = request.files["file"]
        _, path = tempfile.mkstemp()
        logging.info("file path %s", path)
        file.save(path)

        text = run_transcribe(path), 200
        os.remove(path)
        return text
    except Exception as error: # pylint: disable=W0718
        logging.error(traceback.format_exc())
        return f"Transcription failed {error}", 500


# pylint: disable=E0602
@socketio.on("join") 
def join(message):
    """join chat room"""
    username = message["username"]
    room = message["room"]
    join_room(room)

    logging.info("RoomEvent: %s has joined the room %s", username, room)
    emit("ready", {username: username}, to=room, skip_sid=request.sid)


@socketio.on("data")
def transfer_data(message):
    """transfer message"""
    username = message["username"]
    room = message["room"]
    data = message["data"]

    logging.info("RoomEvent: %s has joined the room %s", username, data)
    emit("data", data, to=room, skip_sid=request.sid)


@socketio.on_error_default
def default_error_handler(error):
    """error handler"""
    logging.info("Error: %s", error)
    socketio.stop()

