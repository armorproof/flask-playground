# Imports Flask into Python
from flask import Flask
from flask import render_template

# This object will host the application
app = Flask(__name__)

print("foo")

# Creates a route that calls the following Python function
@app.route("/")
def hello_world():
    name = "Morgan"
    return render_template("index.html", title="Welcome", username = name)

# Not sure what this does exactly, but it ends up running the host's run method
if __name__ == "__main__":
    app.run()