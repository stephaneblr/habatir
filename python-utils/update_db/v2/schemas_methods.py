#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 16:59:08 2018

@author: stephaneblondellarougery
"""

import os
import utils as u

indent = "    "


def init_class(table_name):
    text = "class "+table_name+"Schema(ma.Schema):\n"+indent+"class Meta:\n"+indent+indent+"# Fields to expose\n"
    return text

def end_class(table_name):
    table_name_py = u.jar_to_py(table_name)
    
    text = table_name_py+"_schema = "+table_name+"Schema()\n"
    text += table_name_py+"_schema_many = "+table_name+"Schema(many=True)"
    
    return text

def new_field(col_name):
    f = "'"+col_name+"'"
    return f

def new_schema(table_name, matrix):
    text = init_class(table_name)
    text += indent+indent+"fields = ("
    
    N = len(matrix[0])
    for n in range(0,N):
        col_name = matrix[0][n]
        text += new_field(col_name)
        text += ","
    
    text = text[:-1]
    text += ")\n"
    text += end_class(table_name)
    
    return text    


def create_file_text(db):
    text = "from server import ma\n\n"
    N = u.count_tables(db)
    for n in range(0,N):
        table = db.worksheet('index',n)
        print(str(table.title)+" --> SCHEMA")
        matrix = table.get_all_values()
        text += new_schema(str(table.title), matrix)
        text += "\n\n"
        
    return(text)
    
def create_file(db, base_name):
    
    relative = "generated/for_api/schemas/schemas_" + base_name + ".py"
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, relative)
    
    with open(path, "w") as file:
        python = create_file_text(db)
        file.write(python)