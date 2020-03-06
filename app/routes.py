from flask import request

from app import app
from bot.chatbot import talk


@app.route('/', methods=['POST'])
def index():
    data = request.json
    return {'reply': str(talk(data['message']))}
