#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 08:51:18 2018

@author: stephaneblondellarougery
"""

from flask import render_template
from flaskext.mysql import MySQL
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'mvp'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Uly4Johns18'
app.config['MYSQL_DATABASE_DB'] = 'urbanisme'
app.config['MYSQL_DATABASE_HOST'] = 'bs852543-001.dbaas.ovh.net'
app.config['MYSQL_DATABASE_PORT'] = 35140

mysql.init_app(app)

# Specifiy th swagger configuration file
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

def do_query(query):
    cur = mysql.connect().cursor()
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return r

print(do_query('select * from urbanisme.SUJET'))

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)