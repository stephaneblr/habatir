#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 09:09:01 2018

@author: stephaneblondellarougery
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
configuration = 'mysql+pymysql://mvp:Uly4Johns18@bs852543-001.dbaas.ovh.net:35140/urbanisme'
app.config['SQLALCHEMY_DATABASE_URI'] = configuration
db = SQLAlchemy(app)
ma = Marshmallow(app)




###############################################################################


class Variable(db.Model):
    __tablename__='Variable'
    
    id_variable = db.Column('id_variable', db.Integer, primary_key=True)
    id_parent_variable = db.Column('id_parent_variable', db.Integer)
    nom_variable = db.Column('nom_variable', db.String(100))
    id_sujet = db.Column('id_sujet', db.Integer)
    # Add : db.ForeignKey('Sujet.id_sujet')
    id_destination = db.Column('id_destination', db.Integer)
    est_caracteristique = db.Column('est_caracteristique', db.Boolean)
    est_mimao = db.Column('est_mimao', db.Boolean)
    est_noeud = db.Column('est_noeud', db.Boolean)
    est_variable_relle = db.Column('est_variable_reelle', db.Boolean)
    est_variable_dqr = db.Column('est_variable_dqr', db.Boolean)
    est_variable_enumeration = db.Column('est_variable_enumeration', db.Boolean)
    est_variable_booleenne = db.Column('est_variable_booleenne', db.Boolean)

    def __init__(self, id_variable, id_parent_variable, nom_variable, id_sujet, id_destination, est_caracteristique, est_mimao, est_noeud, est_variable_relle, est_variable_dqr, est_variable_enumeration, est_variable_booleenne):
        self.id_variable = id_variable
        self.id_parent_variable = id_parent_variable
        self.nom_variable = nom_variable
        self.id_sujet = id_sujet
        self.id_destination = id_destination
        self.est_caracteristique = est_caracteristique
        self.est_mimao = est_mimao
        self.est_noeud = est_noeud
        self.est_variable_relle = est_variable_relle
        self.est_variable_dqr = est_variable_dqr
        self.est_variable_enumeration = est_variable_enumeration
        self.est_variable_booleenne = est_variable_booleenne
        
    def __repr__(self):
        return '<Variable {}>'.format(self.id_variable)


class Sujet(db.Model):
    __tablename__='Sujet'
    
    id_sujet = db.Column('id_sujet', db.Integer, primary_key=True)
    id_parent_sujet = db.Column('id_parent_sujet', db.Integer)
    nom_sujet = db.Column('nom_sujet', db.String(100))
    
    #variables = db.relationship('Variable', backref='sujet', lazy='dynamic')

    def __repr__(self):
        return '<Sujet {}>'.format(self.id_sujet)


class Loi(db.Model):
    __tablename__='Loi'
    
    id_loi = db.Column('id_loi', db.Integer, primary_key=True)
    reference_article = db.Column('reference_article', db.String(150))
    branche = db.Column('branche', db.String(150))
    sujet_loi = db.Column('sujet_loi', db.String(150))
    lien = db.Column('lien', db.String(150))


class OutcomeEnum(db.Model):
    __tablename__='OutcomeEnum'
    
    id_variable = db.Column('id_variable', db.Integer, primary_key=True)
    id_outcome = db.Column('id_outcome', db.Integer, primary_key=True)
    nom_outcome = db.Column('nom_outcome', db.String(100))


class ValeurControle(db.Model):
    __tablename__='ValeurControle'
    
    id_valeur_controle = db.Column('id_valeur_controle', db.Integer, primary_key=True)
    id_variable = db.Column('id_variable', db.Integer)
    nom_valeur_controle = db.Column('nom_valeur_controle', db.String(100))
    est_minimum = db.Column('est_minimum', db.Boolean)
    est_identite = db.Column('est_identite', db.Boolean)
    est_maximum = db.Column('est_maximum', db.Boolean)
    est_autorisation = db.Column('est_autorisation', db.Boolean)
    est_obligation = db.Column('est_obligation', db.Boolean)
    est_autre = db.Column('est_autre', db.Boolean)
    

# Get information for meta model prior instanciating the class :
meta_which_destination = 2

class Destination(db.Model):
    t_name = 'Destination'+str(meta_which_destination)
    __tablename__ = t_name
    
    id_destination = db.Column('id_destination', db.Integer, primary_key=True)
    id_parent_destination = db.Column('id_parent_destination', db.Integer)
    nom_destination = db.Column('nom_destination', db.String(150))
    
    



###############################################################################

class VariableSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_variable', 'id_parent_variable', 'nom_variable', 'id_sujet', 'id_destination', 'est_caracteristique', 'est_mimao', 'est_noeud', 'est_variable_relle', 'est_variable_dqr', 'est_variable_enumeration', 'est_variable_booleenne')
variable_schema = VariableSchema()
variables_schema = VariableSchema(many=True)

class SujetSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_sujet', 'id_parent_sujet', 'nom_sujet')       
sujet_schema = SujetSchema()
sujets_schema = SujetSchema(many=True)

class LoiSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_loi', 'reference_article', 'branche', 'sujet_loi', 'lien')       
loi_schema = LoiSchema()
lois_schema = LoiSchema(many=True)

class OutcomeEnumSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_variable', 'id_outcome', 'nom_outcome')       
outcome_enum_schema = OutcomeEnumSchema()
outcome_enum_p_schema = OutcomeEnumSchema(many=True)

class ValeurControleSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_valeur_controle', 'id_variable', 'nom_valeur_controle','est_minimum','est_identite','est_maximum','est_autorisation','est_obligation','est_autre')       
valeur_controle_schema = ValeurControleSchema()
valeur_controle_p_schema = ValeurControleSchema(many=True)

class DestinationSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id_destination', 'id_parent_destination', 'nom_destination')       
destination_schema = DestinationSchema()
destinations_schema = DestinationSchema(many=True)






###############################################################################

# endpoint VARIABLES
@app.route("/variables", methods=["GET"])
def get_variables():
    all_variables = Variable.query.all()
    result = variables_schema.dump(all_variables)
    return jsonify(result.data)
#
#
@app.route("/variables/<id_variable>", methods=["GET"])
def variable_detail(id_variable):
    v = Variable.query.get(id_variable)
    return variable_schema.jsonify(v)



# endpoint SUJETS
@app.route("/sujets", methods=["GET"])
def get_sujets():
    all_sujets = Sujet.query.all()
    result = sujets_schema.dump(all_sujets)
    return jsonify(result.data)
#
# 
@app.route("/sujets/<id_sujet>", methods=["GET"])
def sujet_detail(id_sujet):
    s = Sujet.query.get(id_sujet)
    return sujet_schema.jsonify(s)



# endpoint LOI
@app.route("/lois", methods=["GET"])
def get_lois():
    all_lois = Loi.query.all()
    result = lois_schema.dump(all_lois)
    return jsonify(result.data)
#
# 
@app.route("/lois/<id_loi>", methods=["GET"])
def loi_detail(id_loi):
    l = Loi.query.get(id_loi)
    return loi_schema.jsonify(l)



# endpoint OUTCOME ENUM
@app.route("/outcomes_enums", methods=["GET"])
def get_outcome_enum_p():
    all_outcome_enum_p = OutcomeEnum.query.all()
    result = outcome_enum_p_schema.dump(all_outcome_enum_p)
    return jsonify(result.data)
#
# 
@app.route("/outcomes_enums/<id_variable>/<id_outcome>", methods=["GET"])
def outcome_enum_detail(id_variable,id_outcome):
    # Composite primary key, to figure out.
    return 'Hello World !'



# endpoint VALEURS DE CONTROLE
@app.route("/valeurs_controle", methods=["GET"])
def get_valeur_controle_p():
    all_valeur_controle_p = ValeurControle.query.all()
    result = valeur_controle_p_schema.dump(all_valeur_controle_p)
    return jsonify(result.data)
#
#
@app.route("/valeurs_controle/<id_valeur_controle>", methods=["GET"])
def valeur_controle_detail(id_valeur_controle):
    vc = ValeurControle.query.get(id_valeur_controle)
    return valeur_controle_schema.jsonify(vc)



# endpoint DESTINATION
@app.route("/destinations", methods=["GET"])
def get_destinations():
    all_destinations = Destination.query.all()
    result = destinations_schema.dump(all_destinations)
    return jsonify(result.data)
#
#
@app.route("/destinations/<id_destination>", methods=["GET"])
def destination_detail(id_destination):
    d = Destination.query.get(id_destination)
    return destination_schema.jsonify(d)




###############################################################################

if __name__ == '__main__':
    app.run(debug=True)