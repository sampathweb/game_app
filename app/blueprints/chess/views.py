import random
from flask import Blueprint, render_template, session, request
from flask.ext.socketio import emit, join_room, leave_room
from app import socketio

chess = Blueprint(
    'chess',
    __name__,
    template_folder='templates/chess',
    url_prefix='/chess'
)
socket_name = '/chess/sockets'


@chess.route('/')
def index():
    return render_template('chess/index.html')


@socketio.on('player-move', namespace=socket_name)
def player_move(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('game-response',
         {'data': message['data'], 'count': session['receive_count']},
         room=message['room'])


@socketio.on('join', namespace=socket_name)
def join(message):
    new_game = False
    play_computer = message['data']['play_computer']
    if not message['room']:
        new_game = True
    if new_game:
        game_room = 'game' + str(random.randint(1, 10000))
        marker = 'X'
    else:
        game_room = message['room']
        marker = 'O'
    join_room(game_room)
    session['receive_count'] = session.get('receive_count', 0) + 1
    response_data = {}
    response_data['marker'] = marker
    response_data['room'] = game_room
    response_data['start'] = False
    response_data['count'] = session['receive_count']
    emit('set-room', {'data': response_data})
    # Now broadcast to other player in the room that game can start
    if new_game and not play_computer:
        response_data['start'] = False
        response_data['message'] = 'Waiting for Opponent to Join'
    else:
        response_data['start'] = True
        response_data['move_marker'] = 'X'
    emit('game-start', {'data': response_data}, room=response_data['room'])


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
    emit('game-move',
        {'data': message['data'], 'count': session['receive_count']},
        room=message['room'])


@socketio.on('connect-server', namespace=socket_name)
def connect():
    emit('connect-response', {'data': {'connected': True}})
    emit('msg-response', {'data': {'message': 'Connected to Game Server'}})


@socketio.on('disconnect-server', namespace=socket_name)
def disconnect():
    emit('connect-response', {'data': {'connected': False}})
    emit('msg-esponse', {'data': {'message': 'Dis-connected from Game Server'}})


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
