import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Internet!"

if __name__ == "__main__":
    app.run()
