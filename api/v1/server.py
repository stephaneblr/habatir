#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:37:01 2018

@author: stephaneblondellarougery
"""

from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)

api = Api(app, 
    title='API Urbanis',
    version='0.6',
    description='Version de developpement',
         )

from models import models_urbanisme
from schemas import schemas_urbanisme
# resources imported last
from resources import resources_urbanisme


# Ajout de tous les endpoints semi-automatique

api.add_resource(resources_urbanisme.VariableList, '/variables')
api.add_resource(resources_urbanisme.VariableResource, '/variables/<string:id_variable>')
    


if __name__ == '__main__':
    app.run(debug=True)