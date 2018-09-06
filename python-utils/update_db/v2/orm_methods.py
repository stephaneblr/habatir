#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 16:59:08 2018

@author: stephaneblondellarougery
"""

import model_methods as model
import schemas_methods as schema
import resources_methods as resource
import endpoints_methods as endpoint


def create_files(db, base_name):
    model.create_file(db, base_name)
    schema.create_file(db, base_name)
    resource.create_file(db, base_name)
    endpoint.create_file(db, base_name)
    #simple_mapping(db, base_name) 