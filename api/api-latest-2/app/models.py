#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:37:23 2018

@author: stephaneblondellarougery
"""
from app import db


class Regle(db.Model):
    __tablename__ = 'REGLE'
    
    id_regle = db.Column('id_regle', db.Integer, primary_key = True)
    regle_brute = db.Column('regle_brute', db.String)
    
    run = db.relationships('RegleRun', backref='regle', lazy='dynamic')
    alt = db.relationships('RegleAlt', backref='regle', lazy='dynamic')
    texte = db.relationships('RegleTexte', backref='regle', lazy='dynamic')
    definition = db.relationships('RegleDef', backref='regle', lazy='dynamic')
    contexte = db.relationships('RegleContexte', backref='regle', lazy='dynamic')
    condition = db.relationships('RegleCondition', backref='regle', lazy='dynamic')
    action = db.relationships('RegleAction', backref='regle', lazy='dynamic')
    package = db.relationships('ReglePackage', backref='regle', lazy='dynamic')
    
    def __repr__(self):
        return '<Regle {}>'.format(self.id_regle)


class RegleRun(db.Model):
    __tablename__ = 'REGLE_RUN'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    id_regle = db.Column('id_regle', db.Integer, db.ForeignKey('Regle.id_regle'))
    
    run_true = db.Column('run_true', db.Integer)
    run_except = db.Column('run_except', db.Integer)
    run_mb = db.Column('run_mb', db.Integer)
    run_alt = db.Column('run_alt', db.Integer)
    
    def __repr__(self):
        return '<RegleRun {}>'.format(self.id_regle)
 
    
    
class RegleAlt(db.Model):
    __tablename__ = 'REGLE_ALT'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    id_regle = db.Column('id_regle', db.Integer, db.ForeignKey('Regle.id_regle'))
    
    x = db.Column('y', db.Integer)
    
    def __repr__(self):
        return '<RegleAlt {}>'.format(self.id_regle)

 
    
    
class RegleTexte(db.Model):
    __tablename__ = 'REGLE_TEXTE'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    id_regle = db.Column('id_regle', db.Integer, db.ForeignKey('Regle.id_regle'))
    
    x = db.Column('y', db.Integer)
    
    def __repr__(self):
        return '<RegleTexte {}>'.format(self.id_regle)
    
 
    
    
class RegleDef(db.Model):
    __tablename__ = 'REGLE_DEF'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    id_regle = db.Column('id_regle', db.Integer, db.ForeignKey('Regle.id_regle'))
    
    x = db.Column('y', db.Integer)
    
    def __repr__(self):
        return '<RegleDef {}>'.format(self.id_regle)
    
 
    
    
class RegleContexte(db.Model):
    __tablename__ = 'REGLE_CONTEXTE'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    id_regle = db.Column('id_regle', db.Integer, db.ForeignKey('Regle.id_regle'))
    
    x = db.Column('y', db.Integer)
    
    def __repr__(self):
        return '<RegleContexte {}>'.format(self.id_regle)
    
 
    
    
class RegleCondition(db.Model):
    __tablename__ = 'REGLE_CONDITION'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    id_regle = db.Column('id_regle', db.Integer, db.ForeignKey('Regle.id_regle'))
    
    x = db.Column('y', db.Integer)
    
    def __repr__(self):
        return '<RegleCondition {}>'.format(self.id_regle)
    
 
    
    
class RegleAction(db.Model):
    __tablename__ = 'REGLE_ACTION'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    id_regle = db.Column('id_regle', db.Integer, db.ForeignKey('Regle.id_regle'))
    
    x = db.Column('y', db.Integer)
    
    def __repr__(self):
        return '<RegleAction {}>'.format(self.id_regle)
    
 
    
    
class ReglePackage(db.Model):
    __tablename__ = 'REGLE_PACKAGE'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    id_regle = db.Column('id_regle', db.Integer, db.ForeignKey('Regle.id_regle'))
    
    x = db.Column('y', db.Integer)
    
    def __repr__(self):
        return '<ReglePackage {}>'.format(self.id_regle)