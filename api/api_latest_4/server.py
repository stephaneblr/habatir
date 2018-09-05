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

app = Flask(__name__)
configuration = 'mysql+pymysql://mvp:Uly4Johns18@bs852543-001.dbaas.ovh.net:35140/urbanisme'
app.config['SQLALCHEMY_DATABASE_URI'] = configuration

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

from models import models_urbanisme
from schemas import schemas_urbanisme
    



@api.route('/variables')
class VariableRessource(Resource):
    def get(self):
        all_variables = models_urbanisme.Variable.query.all()
        result = schemas_urbanisme.variables_schema.dump(all_variables)
        return jsonify(result.data)

    
@api.route('/variables/<string:id_variable>')
class VariableList(Resource):
    def get(self, id_variable):
        v = models_urbanisme.Variable.query.get(id_variable)
        return schemas_urbanisme.variable_schema.jsonify(v)
    


if __name__ == '__main__':
    app.run(debug=True)