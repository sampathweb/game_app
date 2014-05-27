from flask import Blueprint, redirect, url_for

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('tic_tac_toe.index'))


@main.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='img/favicon.ico'))
