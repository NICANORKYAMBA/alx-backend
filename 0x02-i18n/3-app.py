#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue July  01 13:00:00 2023

@Author: Nicanor Kyamba
"""
from flask import Flask, render_template, request
from flask_babel import Babel


# Create the config class with default values.
class Config(object):
    """
    Config class.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False


# Instantiate Babel and store it in a module-level variable named babel.
babel = Babel(app)


# Implement the get_locale function using babel.localeselector
# decorator
@babel.localeselector
def get_locale():
    """
    Locale selector function.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Main page
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
