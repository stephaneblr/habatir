#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 17:46:11 2018

@author: stephaneblondellarougery
"""

from flask import Flask, jsonify, request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'mvp'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Uly4Johns18'
app.config['MYSQL_DATABASE_DB'] = 'urbanisme'
app.config['MYSQL_DATABASE_HOST'] = 'bs852543-001.dbaas.ovh.net'
app.config['MYSQL_DATABASE_PORT'] = 35140

mysql.init_app(app)


def do_query(query):
    cur = mysql.connect().cursor()
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return r

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sujets')
def get_sujets():
    return jsonify(do_query('select * from urbanisme.SUJET'))

@app.route('/variables')
def get_variables():
    return jsonify(do_query('select * from urbanisme.VARIABLE'))

if __name__ == '__main__':
    app.run(debug=True)