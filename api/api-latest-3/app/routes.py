#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:37:23 2018

@author: stephaneblondellarougery
"""

from flask import render_template, flash, redirect
from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/test')
def test_models():
    return 'coucou'