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
with open("json/destination.json","r") as fp:
    DESTINATION = json.load(fp)
    

def read_all():
    return [DESTINATION[key] for key in sorted(DESTINATION.keys())]


def read_one(id_destination):
    
    if str(id_destination) in DESTINATION:
        destination = DESTINATION.get(str(id_destination))

    else:
        abort(404, 'DESTINATION with ID {id_destination} not found'.format(
            id_destination=id_destination))

    return destination