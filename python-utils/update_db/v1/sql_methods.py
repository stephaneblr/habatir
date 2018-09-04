#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:28:32 2018

@author: stephaneblondellarougery
"""




# Initialisation et finalisation du fichier
init_sql = """
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

"""



end_sql = """
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
"""


import os


def create_col(col_name, col_type, col_dim, col_special):
    
    special = {}
    special["PK"] = "PRIMARY KEY"
    special["PK - AI"] = "PRIMARY KEY"
    special["FK"] = "DEFAULT NULL" # Les FK ne sont pas encore prises en compte
    special[""] = "DEFAULT NULL"
    
    if col_type == "TINYINT":
        col_dim = "1"
    
    line = "\n  `"+col_name+"` "+col_type.lower()+"("+col_dim+")"+" "+special[col_special]+","
    return line
 
    
def init_table(table_name, arguments):
    request = "CREATE TABLE `"+table_name+"` ("
    data_insert = "INSERT INTO `"+table_name+"` ("
    
    if len(arguments) % 4 == 0:
        N = len(arguments)//4
        
        for n in range(0,N):
            col_name = str(arguments[0+4*n])
            col_type = str(arguments[1+4*n])
            col_dim = str(arguments[2+4*n])
            col_special = str(arguments[3+4*n])
    
            request += create_col(col_name, col_type, col_dim, col_special)
            data_insert+= "`"+col_name+"`, "
            
    else:
        print("Error : Invalid number of argumets.\nPlease specify : col_name | col_type | col_dim | col_special.")
    
    request = request[:-1] # Suppression de la dernière virgule
    request += "\n) ENGINE=InnoDB DEFAULT CHARSET=utf8;"  
        
    data_insert = data_insert[:-2]
    data_insert += ") VALUES"
    
    request += "\n\n"
    request += data_insert
    return request

def is_string(item):
    try:
        int(item)
        return False
    except:
        return True

def quotable(item):
    quotable_item = ""
    for ch in item:
        if ch == "'" :
            quotable_item += "\\"
            quotable_item += "'"
        else:
            quotable_item += ch
    return quotable_item
    
   
def add_data(row):  
    s = "\n("
    for item in row:
        if is_string(item):
            s += "'"
            s += quotable(item)
            s += "'"
        else:
            s += item
        s += ", "
    s = s[:-2]  
    s += "),"
    return s
    
def create_table(table_name, matrix):
    arguments = []
    
    for i in range(0,len(matrix[0])):
        arguments.append(matrix[0][i])
        arguments.append(matrix[2][i])
        arguments.append(matrix[3][i])
        arguments.append(matrix[1][i])
    
    request = init_table(table_name, arguments)
    
    for i in range(4,len(matrix)):
        request += str(add_data(matrix[i]))
    
    request = request[:-1]
    request += ";"
    
    return(request)

def count_tables(db):
    # Le dernier -1 correspond au worksheet 'SQL' à ne pas prendre en compte
    return int(str(db)[len(str(db))-2])-1 

def create_file_request(db):
    request = init_sql
    
    N = count_tables(db)
    for n in range(0,N):
        table = db.worksheet('index',n)
        print(str(table.title)+" --> SQL")
        matrix = table.get_all_values()
        request += create_table(str(table.title), matrix)
        request += "\n\n"
        
    request += end_sql
    return(request)


def create_file(db, file_name):
    
    relative = "sql/" + file_name + ".sql"
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, relative)
    
    with open(path, "w") as file:
        sql = create_file_request(db)
        file.write(sql)