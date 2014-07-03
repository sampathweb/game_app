#!/usr/bin/env python
from app import create_app

env = 'prod'
app = create_app('app.settings.%sConfig' % env.capitalize(), env)

if __name__ == '__main__':
    app.run('0.0.0.0')
