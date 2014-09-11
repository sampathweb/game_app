#!/usr/bin/env python
import os
from flask.ext.script import Manager, Server
from app import create_app, socketio

env = 'dev'
app = create_app('app.settings.%sConfig' % env.capitalize(), env)
app.debug = True

COV = None
if app.config.get('FLASK_COVERAGE'):
    from coverage import coverage
    COV = coverage(branch=True, include='app/*')
    COV.start()

# Start the manager
manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True, use_reloader=True))
manager.add_command("sockrun", socketio.run(app))


@manager.shell
def make_shell_context():
    """Creates a python REPL with several default imports in the context of the app"""
    return dict(app=app)


@manager.command
def test(coverage=False):
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print 'Coverage Summary:'
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print 'HTML Version: file://%s/index.html' % covdir
        COV.erase()


if __name__ == "__main__":
    manager.run()
