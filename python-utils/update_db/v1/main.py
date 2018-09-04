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


# urbanisme
db_urbanisme = gc.open("db_urbanisme")

sql_methods.create_file(db_urbanisme, "urbanisme")
print("SQL file urbanisme.sql succesfully created.")

orm_methods.create_file(db_urbanisme, "urbanisme")
print("ORM file urbanisme.py succesfully created.")



# plu
db_plu = gc.open("db_plu")

sql_methods.create_file(db_plu, "plu")
print("SQL file plu.sql succesfully created.")

orm_methods.create_file(db_plu, "plu")
print("ORM file plu.py succesfully created.")



# plu_tr
db_plu_tr = gc.open("db_plu_tr")

sql_methods.create_file(db_plu_tr, "plu_tr")
print("SQL file plu_tr.sql succesfully created.")

orm_methods.create_file(db_plu_tr, "plu_tr")
print("ORM file plu_tr.py succesfully created.")



# transcription
db_transcription = gc.open("db_transcription")

sql_methods.create_file(db_transcription, "transcription")
print("SQL file transcription.sql succesfully created.")

orm_methods.create_file(db_transcription, "transcription")
print("ORM file transcription.py succesfully created.")







