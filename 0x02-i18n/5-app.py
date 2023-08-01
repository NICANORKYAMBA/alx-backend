#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  01 18:00:00 2023

@Author: Nicanor Kyamba
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


# Supported languages
app.config['LANGUAGE'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


# Mock user table
users = {
    1: {
        'name': 'Balou',
        'locale': 'fr',
        'timezone': 'Europe/Paris'
    },
    2: {
        'name': 'Beyonce',
        'locale': 'en',
        'timezone': 'US/Central'
    },
    3: {
        'name': 'Spock',
        'locale': 'kg',
        'timezone': 'Vulcan'
    },
    4: {
        'name': 'Teletubby',
        'locale': None,
        'timezone': 'Europe/London'
    },
}


def get_user():
    """ Get user by id """
    login_id = request.args.get('login_as')
    if login_id and login_id.isdigit():
        return users[int(login_id)]
    return None


@app.before_request
def before_request():
    """ Before request """
    user_id = get_user()
    g.user = user_id


@babel.localeselector
def get_locale():
    """ Get locale """
    user_locale = request.args.get('locale')
    if user_locale in app.config['LANGUAGE']:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGE'])


@app.route('/')
def index():
    """
    Index page
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
