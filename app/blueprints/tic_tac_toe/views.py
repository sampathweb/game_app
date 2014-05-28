import random
from flask import Blueprint, render_template, session, request
from flask.ext.socketio import emit, join_room, leave_room
from pytic_tac_toe.rules import TicTacToe
from app import socketio

tic_tac_toe = Blueprint(
    'tic_tac_toe',
    __name__,
    template_folder='templates/tic_tac_toe',
    url_prefix='/tic-tac-toe'
)
socket_name = '/tic-tac-toe/sockets'


@tic_tac_toe.route('/')
def index():
    return render_template('tic_tac_toe/index.html')


@socketio.on('player-move', namespace=socket_name)
def player_move(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    data = message['data']
    if data['play_computer']:  # Play Computer
        player_a_choices = []
        player_b_choices = []
        level = data['level']
        for item in data['player_a']:
            row, col = item.split(',')
            player_a_choices.append((int(row), int(col)))
        for item in data['player_b']:
            row, col = item.split(',')
            player_b_choices.append((int(row), int(col)))
        game_toe = TicTacToe(play_computer=True, level=level)
        game_toe.setup_board(player_a_choices, player_b_choices)
        if not game_toe.game_result:
            row, col = game_toe.player_b_move()
            data['move_marker'] = 'O'
            data['last_move'] = str(row) + ',' + str(col)
            if not data['player_b']:
                data['player_b'] = []
            data['player_b'] = data['player_b'].append(data['last_move'])
    emit('game-move',
         {'data': data, 'count': session['receive_count']},
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
    emit('msg-response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
          'count': session['receive_count']})


@socketio.on('room-event', namespace=socket_name)
def room_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('room-move',
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
