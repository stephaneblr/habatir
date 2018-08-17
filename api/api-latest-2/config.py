#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:39:33 2018

@author: stephaneblondellarougery
"""

import os

config_1 = 'mysql://mvp:Uly4Johns18@bs852543-001.dbaas.ovh.net:35140/plu_tr'
config_2 = 'mysql://mvp:Uly4Johns18@bs852543-001.dbaas.ovh.net:35140/urbanisme'
config_3 = 'mysql://mvp:Uly4Johns18@bs852543-001.dbaas.ovh.net:35140/plu'

class Config(object):
    # WTF | Web forms
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Almost deprecated
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQL Alchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or config_1
    SQLALCHEMY_BINDS = {
            'urbanisme' : config_2,
            'plu' : config_3
        }

