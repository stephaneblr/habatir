#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 09:50:50 2018

@author: stephaneblondellarougery
"""
# 3rd party modules
from flask import (
    make_response,
    abort
)

import json


# Data to serve with our API before connecting SQL DB
with open("/Users/stephaneblondellarougery/Desktop/Urbanis/db/db-urbanisme/json.json/VALEUR_CONTROLE.json","r") as fp:
    TEMP_VALEUR_CONTROLE = json.load(fp)

VALEUR_CONTROLE ={}

for item in TEMP_VALEUR_CONTROLE["data"]:
    key = str(item["id-valeur-controle"])
    VALEUR_CONTROLE[key]=item
    

def read_all():
    return [VALEUR_CONTROLE[key] for key in sorted(VALEUR_CONTROLE.keys())]


def read_one(id_valeur_controle):
    
    if str(id_valeur_controle) in VALEUR_CONTROLE:
        valeur_controle = VALEUR_CONTROLE.get(str(id_valeur_controle))

    else:
        abort(404, 'Valeur de controle with ID {id_valeur_controle} not found'.format(
            id_valeur_controle=id_valeur_controle))

    return valeur_controle