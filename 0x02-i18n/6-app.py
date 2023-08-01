#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  01 19:00:00 2023

@Author: Nicanor Kyamba
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# Supported languages
app.config['LANGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Get user by id"""
    return users.get(user_id)


@app.before_request
def before_request():
    """Get user by id"""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id and user_id.isdigit() else None


@babel.localeselector
def get_locale():
    """Get the locale from the request"""
    # Get the locale from URL parameters
    user_locale = request.args.get('locale')
    if user_locale and user_locale in app.config['LANGUAGES']:
        return user_locale

    # Get the locale from the user settings
    if g.user and 'locale' in g.user and \
            g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Get the locale from the request header
    request_locale = request.accept_languages.best_match(
            app.config['LANGUAGES'])
    if request_locale:
        return request_locale

    # Fallback to the default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """Index page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
