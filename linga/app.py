""" flask app """
from flask import Flask

app = Flask(__name__, "/static")


@app.route("/")
def get_canvas():
    """ return static content """
    return app.send_static_file("index.html")
