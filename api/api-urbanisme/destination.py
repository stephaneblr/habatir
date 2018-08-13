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

with open("/Users/stephaneblondellarougery/Desktop/Urbanis/db/db-urbanisme/json.json/DESTINATION_2.json","r") as fp:
    TEMP_DESTINATION = json.load(fp)

DESTINATION ={}

for item in TEMP_DESTINATION["data"]:
    key = str(item["id-destination"])
    DESTINATION[key]=item
 
    
    

def read_all():
    return [DESTINATION[key] for key in sorted(DESTINATION.keys())]


def read_one(id_destination):
    
    if str(id_destination) in DESTINATION:
        destination = DESTINATION.get(str(id_destination))

    else:
        abort(404, 'DESTINATION with ID {id_destination} not found'.format(
            id_destination=id_destination))

    return destination