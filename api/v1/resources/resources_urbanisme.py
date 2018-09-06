#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:37:01 2018

@author: stephaneblondellarougery
"""

from flask import jsonify
from flask_restplus import Resource

from server import models_urbanisme, schemas_urbanisme


###


class VariableList(Resource):
    def get(self):
        all_variables = models_urbanisme.Variable.query.all()
        result = schemas_urbanisme.variables_schema.dump(all_variables)
        return jsonify(result.data)

    
class VariableResource(Resource):
    def get(self, id_variable):
        v = models_urbanisme.Variable.query.get(id_variable)
        return schemas_urbanisme.variable_schema.jsonify(v)
    