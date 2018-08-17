#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:37:23 2018

@author: stephaneblondellarougery
"""

from flask import render_template, flash, redirect
from app import app
from app.forms_test import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    
    return render_template('login.html', title='Sign In', form=form)