import random
from flask import Blueprint, render_template, session, request
from flask.ext.socketio import emit, join_room, leave_room
from app import socketio

tic_tac_toe = Blueprint(
    'tic_tac_toe',
    __name__,
    template_folder='templates/tic_tac_toe',
    url_prefix='/tic-tac-toe'
)
socket_name = '/tic-tac-toe/sockets'


#@tic_tac_toe.route('/', method=['GET', 'POST'])
@tic_tac_toe.route('/')
def index():
    # if request.method == 'POST' and form.validate_on_submit():
      # Get the moves
      # Instanciate the moves
      # get Next Move
    return render_template('tic_tac_toe/index.html')


@tic_tac_toe.route('/<room>/')
def index_room(room):
    message = {}
    message['room'] = room
    join(message)
    return render_template('tic_tac_toe/index.html', room=room)


@socketio.on('player-move', namespace=socket_name)
def player_move(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('game-response',
         {'data': message['data'], 'count': session['receive_count']},
         room=message['room'])


@socketio.on('my-event', namespace=socket_name)
def my_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('response',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.on('broadcast-event', namespace=socket_name)
def broadcast_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socketio.on('join', namespace=socket_name)
def join(message):
    response_data = {}
    response_data['room'] = message['room']
    if not response_data['room']:
        response_data['room'] = 'game' + str(random.randint(1, 10000))
    join_room(response_data['room'])
    response_data['game_url'] = request.url + response_data['room']
    session['receive_count'] = session.get('receive_count', 0) + 1
    response_data['data'] = 'In rooms: ' + ', '.join(request.namespace.rooms) + response_data['game_url']
    response_data['count'] = session['receive_count']
    emit('response', response_data)


# @socketio.on('join', namespace=socket_name)
# def join(message):
#     response_data = {}
#     if 'room' in message:
#         response_data['room'] = message['room']
#     else:
#         response_data['room'] = 'game' + str(random.randint(1, 10000))
#     join_room(response_data['room'])
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     response_data['data'] = 'In rooms: ' + ', '.join(request.namespace.rooms) + response_data['game_url']
#     response_data['count'] = session['receive_count']
#     emit('response', response_data)


@socketio.on('leave', namespace=socket_name)
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
          'count': session['receive_count']})


@socketio.on('room-event', namespace=socket_name)
def room_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('response',
        {'data': message['data'], 'count': session['receive_count']},
        room=message['room'])


@socketio.on('connect', namespace=socket_name)
def connect():
    emit('response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace=socket_name)
def disconnect():
    print 'Client disconnected'
