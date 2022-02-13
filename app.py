from flask import Flask
from env import API_KEY

app = Flask(__name__)


@app.route('/')
