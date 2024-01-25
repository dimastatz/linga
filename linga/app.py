""" flask app """
import logging
import traceback
import tempfile, os
from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room
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
        file = request.files['file']
        filed, path = tempfile.mkstemp()
        logging.info(f"file path{filed}, {path}")
        file.save(path)

        text = run_transcribe(path), 200
        os.remove(path)
        return text
    except Exception as e:
        logging.error(traceback.format_exc())
        return f"Transcription failed {e}", 500


@socketio.on('join')
def join(message):
    """join chat room"""
    username = message['username']
    room = message['room']
    join_room(room)
    print('RoomEvent: {} has joined the room {}\n'.format(username, room))
    emit('ready', {username: username}, to=room, skip_sid=request.sid)


@socketio.on('data')
def transfer_data(message):
    """transfer message"""
    username = message['username']
    room = message['room']
    data = message['data']
    print('DataEvent: {} has sent the data:\n {}\n'.format(username, data))
    emit('data', data, to=room, skip_sid=request.sid)
