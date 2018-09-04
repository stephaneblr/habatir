#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 16:59:08 2018

@author: stephaneblondellarougery
"""

import os

indent = "    "

def init_class(table_name):
    text = "class "+table_name+"(db.Model):\n"+indent+"__tablename__='"+table_name+"'"
    return text

def get_type(col_type, col_dim):
    if col_type == "VARCHAR":
        return "db.String("+str(col_dim)+")"
    elif col_type == "INT":
        return "db.Integer"
    elif col_type == "TINYINT":
        return "db.Boolean"
    else:
        return "Error : Invalid column type"
    
def is_special(col_special):
    return (col_special == "PK") | (col_special == "PK - AI")
    
def get_special(col_special):
    return "primary_key=True"

def new_line(col_name, col_type, col_dim, col_special):
    line = "\n"+indent+col_name+" = db.Column('" + col_name + "', " 
    line += get_type(col_type, col_dim)
    if is_special(col_special):
        line += ", "
        line += get_special(col_special)
    line += ")"
    return line

def new_class(table_name, matrix):
    text = init_class(table_name)
    text += "\n"
    
    N = len(matrix[0])
    for n in range(0,N):
        col_name = matrix[0][n]
        col_type = matrix[2][n]
        col_dim = matrix[3][n]
        col_special = matrix[1][n]
        
        text += new_line(col_name, col_type, col_dim, col_special)
    return text    

def count_tables(db):
    # Le dernier -1 correspond au worksheet 'SQL' à ne pas prendre en compte
    try:
        count = int(str(db)[len(str(db))-3:len(str(db))-1])-1 
        return count
    except:
        return int(str(db)[len(str(db))-2])-1 

def create_file_text(db):
    text = ""
    N = count_tables(db)
    for n in range(0,N):
        table = db.worksheet('index',n)
        print(str(table.title)+" --> ORM")
        matrix = table.get_all_values()
        text += new_class(str(table.title), matrix)
        text += "\n\n"
        
    return(text)
    
def create_file(db, file_name):
    
    relative = "orm/" + file_name + ".py"
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, relative)
    
    with open(path, "w") as file:
        python = create_file_text(db)
        file.write(python)