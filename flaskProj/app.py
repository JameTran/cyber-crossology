from flask import Flask
from datetime import datetime
import re
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return 0

@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

# Filter the name argument to letters only using regular expressions. URL arguments
# can contain arbitrary text, so we restrict to safe characters only.
match_object = re.match("[a-zA-Z]+", name)

if match_object:
    clean_name = match_object.group(0)
else:
    clean_name = "Friend"

content = "Hello there, " + clean_name + "! It's " + formatted_now
return content