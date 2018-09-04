#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 11:42:29 2018

@author: stephaneblondellarougery
"""


import sql_methods
import orm_methods
import pygsheets

gc = pygsheets.authorize(service_file='/Users/stephaneblondellarougery/Desktop/client_secret/client_secret_python_utils.json')
print('Python_parser is now connected with Drive API and Sheets API.\n')    


# Urbanisme
db_urbanisme = gc.open("db_urbanisme_fk")

sql_methods.create_file(db_urbanisme, "urbanisme")
print("SQL file urbanisme.sql succesfully created.")

orm_methods.create_file(db_urbanisme, "urbanisme")
print("ORM file urbanisme.py succesfully created.")




