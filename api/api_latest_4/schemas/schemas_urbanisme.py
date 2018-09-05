#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:37:01 2018

@author: stephaneblondellarougery
"""

from server import ma

class VariableSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_variable', 'id_parent_variable', 'nom_variable', 'id_sujet', 'id_destination', 'est_caracteristique', 'est_mimao', 'est_noeud', 'est_variable_relle', 'est_variable_dqr', 'est_variable_enumeration', 'est_variable_booleenne')
variable_schema = VariableSchema()
variables_schema = VariableSchema(many=True)
