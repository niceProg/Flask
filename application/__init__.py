from flask import Flask
from chatterbot import ChatBot

app = Flask(__name__)
bot = ChatBot("Python-BOT")

from application import routes