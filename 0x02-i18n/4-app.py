#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  01 17:00:00 2023

@Author: Firstname Lastname
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

app.config['LANGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@babel.localeselector
def get_locale():
    """
    Returns the best match for the user's locale
    """
    # Check if 'locale' parameter is present in the request's
    # query string
    locale = request.args.get('locale')

    # If the 'locale' parameter is valid and supported, return it
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Resort to the default behaviour if 'locale' parameter is not present
    # or not valid
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Index page"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
