import random
from flask import Blueprint, render_template, session, request
from flask.ext.socketio import emit, join_room, leave_room
from app import socketio

checkers = Blueprint(
    'checkers',
    __name__,
    template_folder='templates/checkers',
    url_prefix='/checkers'
)
socket_name = '/checkers/sockets'


@checkers.route('/')
def index():
    return render_template('checkers/index.html')

