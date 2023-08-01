#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue July  01 11:40:00 2023

@Author: Nicanor Kyamba
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Instatiate Babel and store it in a module-level variable
# named babel
babel = Babel(app)


# Create the config class with LANGUAGES and other
# configurations
class Config:
    """
    The config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Create a new instance of the config class
app.config.from_object(Config)


@app.route('/')
def index():
    """
    The home page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
