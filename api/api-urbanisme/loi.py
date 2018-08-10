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
with open("json/loi.json","r") as fp:
    LOI = json.load(fp)
    

def read_all():
    return [LOI[key] for key in sorted(LOI.keys())]


def read_one(id_loi):
    
    if str(id_loi) in LOI:
        loi = LOI.get(str(id_loi))

    else:
        abort(404, 'LOI with ID {id_loi} not found'.format(
            id_loi=id_loi))

    return loi