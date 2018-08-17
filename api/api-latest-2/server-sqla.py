#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 17:46:11 2018

@author: stephaneblondellarougery
"""



from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



app = Flask(__name__)
CORS(app)


# SQL Alchemy config 

config_1 = 'mysql://mvp:Uly4Johns18@bs852543-001.dbaas.ovh.net:35140/plu_tr'
config_2 = 'mysql://mvp:Uly4Johns18@bs852543-001.dbaas.ovh.net:35140/urbanisme'
config_3 = 'mysql://mvp:Uly4Johns18@bs852543-001.dbaas.ovh.net:35140/plu'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config_1
app.config['SQLALCHEMY_BINDS'] = {
            'urbanisme' : config_2,
            'plu' : config_3
        }

db = SQLAlchemy(app)



# Map tables to pyhton objects

class RegleRun(db.Model):
    __tablename__ = 'regle_run'
    
    id_regle = db.Column('id_regle', db.Integer, primary_key = True)
    run_true = db.Column('run_true', db.Integer)
    run_except = db.Column('run_except', db.Integer)
    run_mb = db.Column('run_mb', db.Integer)
    run_alt = db.Column('run_alt', db.Integer)
    
    def __repr__(self):
        return '<Regle %r>' % self.id_regle









# Run in development mode

if __name__ == '__main__':
    app.run(debug=True)