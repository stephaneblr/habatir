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
with open("/Users/stephaneblondellarougery/Desktop/Urbanis/db/db-urbanisme/json.json/VARIABLE.json","r") as fp:
    TEMP_VARIABLE = json.load(fp)

VARIABLE ={}

for item in TEMP_VARIABLE["data"]:
    key = str(item["id-variable"])
    VARIABLE[key]=item
    
    

def read_all():
    """
    This function responds to a request for /api/variable
    with the complete lists of variable
    :return:        json string of list of people
    """
    # Create the list of people from our data
    return [VARIABLE[key] for key in sorted(VARIABLE.keys())]


def read_one(id_variable):
    """
    This function responds to a request for /api/variable/{id_variable}
    with one matching id from variable dictionary
    :param id_variable:   id of variable to find
    :return:        variable matching id
    """
    # Does the person exist in people?
    if str(id_variable) in VARIABLE:
        variable = VARIABLE.get(str(id_variable))

    # otherwise not found
    else:
        abort(404, 'Variable with ID {id_variable} not found'.format(
            id_variable=id_variable))

    return variable


# Unused
def read_children(id_parent):
    """
    This function responds to a request for /api/variable/{id_parent}
    with one matching id from variable dictionary
    :param id_parent:   id of variable children to find
    :return:        variable matching id_parent
    """
    
    KEYLIST = []
    
    for key, value_body in VARIABLE.items():
        if value_body['id_parent'] == id_parent :
            KEYLIST.append(key)
            
    if KEYLIST == []:
        abort(404, 'Variable with PARENT ID {id_parent} does not exist or has no children.'.format(
            id_parent=id_parent))
        
    else :   
        return [VARIABLE[key] for key in KEYLIST]