from flask import Flask
from markupsafe import escape
app = Flask(__name__)
app.debug = True
@app.route("/")
def hello_world():
    return "<p>Hello, Apr 22 and Sept 22 DSML Batch!</p>"



@app.route("/ping")
def ping():
    return "<p>Hello This is ping</p>"


@app.route("/user/<username>")
def user(username):
    return "<p>Hello {}</p>".format(escape(username))


