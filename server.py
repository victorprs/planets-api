from flask import Flask
app = Flask(__name__)

@app.route('/')
def empty_page():
    return "No content"