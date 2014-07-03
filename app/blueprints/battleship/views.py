import random
from flask import Blueprint, render_template, session, request
from flask.ext.socketio import emit, join_room, leave_room
from app import socketio

battleship = Blueprint(
    'battleship',
    __name__,
    template_folder='templates/battleship',
    url_prefix='/battleship'
)
socket_name = '/battleship/sockets'


@battleship.route('/')
def index():
    return render_template('battleship/index.html')

