#! ../env/bin/python
from flask import Flask
from flask.ext.socketio import SocketIO

socketio = SocketIO()


def create_app(object_name, env):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. appname.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__)

    app.config.from_object(object_name)
    app.config['ENV'] = env

    # Initialize socketio
    socketio.init_app(app)

    # register our blueprints
    from app.blueprints import main, tic_tac_toe, battleship, checkers, chess
    app.register_blueprint(main)
    app.register_blueprint(tic_tac_toe)
    app.register_blueprint(battleship)
    app.register_blueprint(checkers)
    app.register_blueprint(chess)

    return app
