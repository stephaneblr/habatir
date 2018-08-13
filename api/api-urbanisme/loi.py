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


# Get JSON data 

with open("/Users/stephaneblondellarougery/Desktop/Urbanis/db/db-urbanisme/json.json/LOI.json","r") as fp:
    TEMP_LOI = json.load(fp)

LOI ={}

for item in TEMP_LOI["data"]:
    key = str(item["id-loi"])
    LOI[key]=item
    
    
    

def read_all():
    return [LOI[key] for key in sorted(LOI.keys())]


def read_one(id_loi):
    
    if str(id_loi) in LOI:
        loi = LOI.get(str(id_loi))

    else:
        abort(404, 'LOI with ID {id_loi} not found'.format(
            id_loi=id_loi))

    return loi