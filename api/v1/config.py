#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:39:33 2018

@author: stephaneblondellarougery
"""

import os

config_1 = 'mysql+pymysql://mvp:Uly4Johns18@bs852543-001.dbaas.ovh.net:35140/plu_tr'
config_2 = 'mysql+pymysql://mvp:Uly4Johns18@bs852543-001.dbaas.ovh.net:35140/urbanisme'
config_3 = 'mysql+pymysql://mvp:Uly4Johns18@bs852543-001.dbaas.ovh.net:35140/plu'
config_4 = 'mysql+pymysql://mvp:Uly4Johns18@bs852543-001.dbaas.ovh.net:35140/transcription'

class Config(object):

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = config_2
    
    SQLALCHEMY_BINDS = {
            'plu_tr' : config_1,
            'plu' : config_3, 
            'transcription' : config_4
        }

