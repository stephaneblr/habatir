#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 16:59:08 2018

@author: stephaneblondellarougery
"""

import os
import utils as u

indent = "    "

def new_ressource_list(table_name, base_name):
    table_name_py = u.jar_to_py(table_name)

    text = "class "+table_name+"List(Resource):\n"
    text += indent+"def get(self):\n"
    text += indent+indent+"all = models_"+base_name+"."+table_name+".query.all()\n"
    text += indent+indent+"result = schemas_"+base_name+"."+table_name_py+"_schema_many.dump(all)\n"
    text += indent+indent+"return jsonify(result.data)"
    
    return text 

def new_ressource(table_name, base_name):
    table_name_py = u.jar_to_py(table_name)
    
    text = "class "+table_name+"Resource(Resource):\n"
    text += indent+"def get(self, id_"+table_name_py+"):\n"
    text += indent+indent+"one = models_"+base_name+"."+table_name+".query.get(id_"+table_name_py+")\n"
    text += indent+indent+"return schemas_"+base_name+"."+table_name_py+"_schema.jsonify(one)\n"
    
    return text


def create_file_text(db, base_name):
    text = "from flask import jsonify\n"
    text += "from flask_restplus import Resource\n"
    text += "from server import models_"+base_name+"\n"
    text += "from server import schemas_"+base_name+"\n"
    text += "\n"
    
    N = u.count_tables(db)
    for n in range(0,N):
        table = db.worksheet('index',n)
        print(str(table.title)+" --> RESOURCE")
        text += new_ressource_list(str(table.title), base_name)
        text += "\n"
        text += new_ressource(str(table.title), base_name)
        text += "\n\n"
        
    return(text)
    
def create_file(db, base_name):
    
    relative = "generated/for_api/resources/resources_" + base_name + ".py"
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, relative)
    
    with open(path, "w") as file:
        python = create_file_text(db, base_name)
        file.write(python)