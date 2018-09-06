#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:37:01 2018

@author: stephaneblondellarougery
"""

from server import db

class Variable(db.Model):
    __tablename__='Variable'
    
    id_variable = db.Column('id_variable', db.Integer, primary_key=True)
    id_parent_variable = db.Column('id_parent_variable', db.Integer)
    nom_variable = db.Column('nom_variable', db.String(100))
    id_sujet = db.Column('id_sujet', db.Integer)
    # Add : db.ForeignKey('sujet.id_sujet')
    id_destination = db.Column('id_destination', db.Integer)
    est_caracteristique = db.Column('est_caracteristique', db.Boolean)
    est_mimao = db.Column('est_mimao', db.Boolean)
    est_noeud = db.Column('est_noeud', db.Boolean)
    est_variable_relle = db.Column('est_variable_reelle', db.Boolean)
    est_variable_dqr = db.Column('est_variable_dqr', db.Boolean)
    est_variable_enumeration = db.Column('est_variable_enumeration', db.Boolean)
    est_variable_booleenne = db.Column('est_variable_booleenne', db.Boolean)
    
    
