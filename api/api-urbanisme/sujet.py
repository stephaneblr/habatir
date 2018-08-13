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
with open("/Users/stephaneblondellarougery/Desktop/Urbanis/db/db-urbanisme/json.json/SUJET.json","r") as fp:
    TEMP_SUJET = json.load(fp)

SUJET ={}

for item in TEMP_SUJET["data"]:
    key = str(item["id-sujet"])
    SUJET[key]=item
    

def read_all():
    return [SUJET[key] for key in sorted(SUJET.keys())]


def read_one(id_sujet):
    
    if str(id_sujet) in SUJET:
        sujet = SUJET.get(str(id_sujet))

    else:
        abort(404, 'Sujet with ID {id_sujet} not found'.format(
            id_sujet=id_sujet))

    return sujet
