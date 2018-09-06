#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 16:59:08 2018

@author: stephaneblondellarougery
"""

import os
import utils as u 
import uuid

indent = "    "

def new_endpoint(table_name, base_name,id):
    table_name_py = u.jar_to_py(table_name)
    table_name_py_plur = u.plural(u.jar_to_py(table_name))
    
    text = "ns"+str(id)+".add_resource(resources_"+base_name+"."+table_name+"List, '/"+table_name_py_plur+"')\n"
    text += "ns"+str(id)+".add_resource(resources_"+base_name+"."+table_name+"Resource, '/"+table_name_py_plur+"/<string:id_"+table_name_py+">')\n"
    
    return text
    

def init_list(id,base_name):
    text = "ns"+str(id)+" = Namespace('"+base_name+"', description='Ressources "+base_name+"')\n"
    return text

def end_list(id):
    return "api.add_namespace(ns"+str(id)+")\n"


def create_file_text(db, base_name):
    ID = {
            "urbanisme" : 1,
            "plu" : 10,
            "plu_tr" : 100,
            "transcription" : 1000,
        }
    id = ID[base_name]
    
    text = "from resources import resources_"+base_name+"\n"
    text += "\n"
    text += init_list(id,base_name)
    text += "\n"
    
    N = u.count_tables(db)
    for n in range(0,N):
        table = db.worksheet('index',n)
        print(str(table.title)+" --> ENDPOINT")
        text += new_endpoint(str(table.title), base_name,id)
        text += "\n"
        
    text += end_list(id)
        
    return(text)
    
def create_file(db, base_name):
    
    relative = "generated/for_api/add_to_server/" + base_name + ".py"
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, relative)
    
    with open(path, "w") as file:
        python = create_file_text(db, base_name)
        file.write(python)