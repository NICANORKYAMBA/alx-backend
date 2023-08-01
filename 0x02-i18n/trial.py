#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue July 01 13:00:00 2023

@Author: Nicanor Kyamba
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Main page
    """
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
