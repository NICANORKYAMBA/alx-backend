#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue July  01 12:00:00 2023

@Author: Nicanor Kyamba
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Instatiate the Babel class and store it in a module-level
# variable called babel
babel = Babel(app)


# Create the Config class with the default values
class Config:
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


# Implement the get_locale() function using
# babel.localeselector() decorator
@babel.localeselector
def get_locale():
    """Get the current locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Main page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
